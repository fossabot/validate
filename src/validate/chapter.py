import argparse
import requests
import os
import time
import sys

MAIN_URL = 'https://www.datacamp.com/api/courses/'
PARSER_URL = 'https://teach-parser.new.datacamp.com/api/parse'
IMB_URL_FMT = 'https://imb.datacamp.com/active_image/%s/%s'
VALIDATOR_URL = 'https://validator.datacamp.com/'

def get(url):
    resp = requests.get(url)
    assert resp.status_code == 200
    return resp.json()

def post(url, payload):
    resp = requests.post(url, json=payload)
    assert resp.status_code == 200
    return resp.json()

def validate_chapter(course_id,
                     chapter_file,
                     key = None):
    
    print('figuring out programming language ...')
    programming_language = get(MAIN_URL + course_id)['programming_language'] or 'test'


    print('parsing chapter file ...')
    if not os.path.exists(chapter_file):
        raise ValueError('The chapter file you referenced does not exist')

    with open(chapter_file, 'r') as fp:
        read_lines = fp.readlines()
        chapter_content = '\n'.join(read_lines)

    parse_resp = post(PARSER_URL, payload = {'file': chapter_content})
    exercises = parse_resp['exercises']

    print('selecting only NormalExercise exercises')
    exercises = [ ex for ex in exercises if ex['type'] == 'NormalExercise' ]

    if key:
        print('selecting exercise with key %s ...' % key)
        exercises = [ ex for ex in exercises if ex['key'] == key ]
        assert len(exercises) == 1
    
    print('figuring out active course image ...')
    imb_resp = requests.get(IMB_URL_FMT % ('course', course_id))
    assert imb_resp.status_code == 200
    image = imb_resp.text

    print('sending testing payload to validator ...')
    # drop some stuff the validator can't take
    for i in range(len(exercises)):
        for el in ['chunkLines', 'tags', 'definedBy']:
            if el in exercises[i]:
                del exercises[i][el]

    validator_payload = { 'image':image, 'programming_language':programming_language, 'exercises':exercises }
    validator_key = post(VALIDATOR_URL + 'test', payload=validator_payload)['key']

    print('polling for validator results ...')
    report = get(VALIDATOR_URL + 'poll/' + validator_key)
    while not report['finished']:
        time.sleep(1)
        print('.')
        report = get(VALIDATOR_URL + 'poll/' + validator_key)

    # INTERPRET RESULTS
    all_passed = all([ x['result']['success'] for x in report['results'].values() ])
    if all_passed:
        print('SUCCESS: all testing passed correctly!')
    else:
        print('FAILURE: some exercises failed')

    print('Visit the validator logs at %s' % VALIDATOR_URL + 'logs/' + validator_key)
      
    return(all_passed)

def main():
    parser = argparse.ArgumentParser(description='Test one or more exercises in a chapter file on your computer against the validator.')
    parser.add_argument('course_id', type=str,
                        help='ID of the course you are testing (required to figure out active image)')
    parser.add_argument('chapter_file', type=str,
                        help='path to the chapter file that contains the exercise you want to parse.')
    parser.add_argument('--key', '-k', dest='key', default=None,
                        help='key of the exercise, if you only want to test a specific exercise')

    args = parser.parse_args()    
    validate_chapter(**vars(args))

