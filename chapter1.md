---
title_meta: Chapter 1
title: Conditionals and Control Flow
description: To be TRUE or not be TRUE, that's the question. In this chapter you'll
  learn about relational operators to see how R objects compare and logical operators
  to combine logicals. Next, you'll use this knowledge to build conditional statements.
attachments:
  slides_link: https://s3.amazonaws.com/assets.datacamp.com/course/intermediate_r/intermediate_r_ch1_slides.pdf
free_preview: yes

---

## Relational Operators



```yaml
type: VideoExercise
lang: r
xp: 50
skills: '1'
key: 9af3e6d86523573ebe761f674cb92f849b61898e
video_link: |
  //player.vimeo.com/video/160339466
video_hls: |
  //videos.datacamp.com/transcoded/672_intermediate_r/v2/hls-ch1_1.master.m3u8
```


`@projector_key`
70a435759e8345075c6f0189371b724a



---

## Equality


```yaml
type: NormalExercise
lang: r
xp: 100
skills: '1'
key: 82003a4d2853e2b847d5bdfe9503209614315bcd
```


The most basic form of comparison is equality. Let's briefly recap its syntax. The following statements all evaluate to `TRUE` (feel free to try them out in the console).

```
3 == (2 + 1)
"intermediate" != "r"
TRUE != FALSE
"Rchitect" != "rchitect"
```

Notice from the last expression that R is case sensitive: "R" is not equal to "r". Keep this in mind when solving the exercises in this chapter!

`@instructions`

- In the editor on the right, write R code to see if `TRUE` equals `FALSE`.
- Likewise, check if `-6 * 14` is _not_ equal to `17 - 101`.
- Next up: comparison of character strings. Ask R whether the strings "useR" and "user" are equal.
- Finally, find out what happens if you compare logicals to numerics: are `TRUE` and 1 equal?

`@hint`

In the final instruction, you don't need additional steps to carry out the comparison; just use the same operators as before.

`@pre_exercise_code`

```{r}
# no pec
```

`@sample_code`

```{r}
# Comparison of logicals


# Comparison of numerics


# Comparison of character strings


# Compare a logical with a numeric


```

`@solution`

```{r}
# Comparison of logicals
TRUE == FALSE

# Comparison of numerics
-6 * 14 != 17 - 101

# Comparison of character strings
"useR" == "user"

# Compare a logical with a numeric
TRUE == 1
```

`@sct`

```{r}
test_error()
test_student_typed(strings = c("TRUE == FALSE", "FALSE == TRUE"),
                   not_typed_msg = "Have another look at the comparison of logicals. You should use `TRUE == ___`; can you fill in the `___`?")
test_student_typed(strings = c("-6 * 14 != 17 - 101", "17 - 101 != -6 * 14", "(-6 * 14) != (17 - 101)", "(17 - 101) != (-6 * 14)"),
                   not_typed_msg = "Have a closer look at the comparison of numerics (second instruction). You should use `-6 * 14 != ___ - ___`, can you fill in the missing parts?")
test_student_typed(strings = c("\"useR\" == \"user\"", "\"user\" == \"useR\""),
                   not_typed_msg = "Check your code for the comparison of character strings again. You should see whether `\"useR\"` and `\"user\"` are equal (`==`).")
test_student_typed(strings = c("TRUE == 1", "1 == TRUE"),
                   not_typed_msg = "Have you correctly compared `TRUE` with `1` using the equality operator (`==`)?")

success_msg("Awesome! Since `TRUE` coerces to `1` under the hood, `TRUE == 1` evaluates to `TRUE`. Make sure not to mix up `==` (comparison) and `=` (assignment), `==` is what need to check the equality of R objects.")
```

---

## Greater and less than


```yaml
type: NormalExercise
lang: r
xp: 100
skills: '1'
key: 0ef596baa98b7e37ca06b768ad5ee9b801802947
```


Apart from equality operators, Filip also introduced the _less than_ and _greater than_ operators: `<` and `>`. You can also add an equal sign to express _less than or equal to_ or _greater than or equal to_, respectively. Have a look at the following R expressions, that all evaluate to `FALSE`:

```
(1 + 2) > 4
"dog" < "Cats"
TRUE <= FALSE
```

Remember that for string comparison, R determines the _greater than_ relationship based on alphabetical order. Also, keep in mind that `TRUE` corresponds to `1` in R, and `FALSE` coerces to `0` behind the scenes. Therefore, `FALSE < TRUE` is `TRUE`.

`@instructions`

Write R expressions to check whether:

- `-6 * 5 + 2` is greater than or equal to `-10 + 1`.
- "raining" is less than or equal to "raining dogs".
- TRUE is greater than FALSE.

`@hint`

A correct answer to the second instruction would be:

```
"raining" <= "raining dogs"
```

`@pre_exercise_code`

```{r}
# no pec
```

`@sample_code`

```{r}
# Comparison of numerics


# Comparison of character strings


# Comparison of logicals

```

`@solution`

```{r}
# Comparison of numerics
-6 * 5 + 2 >= -10 + 1

# Comparison of character strings
"raining" <= "raining dogs"

# Comparison of logicals
TRUE > FALSE
```

`@sct`

```{r}
test_error()
test_student_typed(strings = c("- 6 * 5 + 2 >= -10 + 1", "-10 + 1 <= - 6 * 5 + 2",
                               "(- 6 * 5 + 2) >= (-10 + 1)", "(-10 + 1) <= - (6 * 5 + 2)",
                               "(- 6 * 5 + 2) >= -10 + 1", "- 6 * 5 + 2 >= (-10 + 1)"),
                   not_typed_msg = "Have another look at the comparison of numerics part of your submission. You should use something like `-6 * 5 + 2 >= ___`; can you fill in the missing parts?")
test_student_typed(strings = c("\"raining\" <= \"raining dogs\"", "\"raining dogs\" >= \"raining\""),
                   not_typed_msg = "There's something wrong with the comparison of character strings. You should use something like `\"raining\" <= ___`; can you fill in the missing parts?")
test_student_typed(strings = c("TRUE > FALSE", "FALSE < TRUE"),
                   not_typed_msg = "The comparison of logical parts is not correct. `TRUE > ___` is part of the solution, up to you to fill in the `___`. Try again!")

success_msg("Great job! Make sure to have a look at the console output to see if R returns the results you expected.")
```

---

## Compare vectors


```yaml
type: NormalExercise
lang: r
xp: 100
skills: '1'
key: 7cebe4af13c64d4118b46846204eeb3bbad25131
```


You are already aware that R is very good with vectors. Without having to change anything about the syntax, R's relational operators also work on vectors.

Let's go back to the example that was started in the video. You want to figure out whether your activity on social media platforms have paid off and decide to look at your results for LinkedIn and Facebook. The sample code in the editor initializes the vectors `linkedin` and `facebook`. Each of the vectors contains the number of profile views your LinkedIn and Facebook profiles had over the last seven days.

`@instructions`

Using relational operators, find a logical answer, i.e. `TRUE` or `FALSE`, for the following questions:

- On which days did the number of LinkedIn profile views exceed 15?
- When was your LinkedIn profile viewed only 5 times or fewer?
- When was your LinkedIn profile visited more often than your Facebook profile?

`@hint`

Let's get you up to speed with a comparable example. To see when your LinkedIn profile was viewed more than 10 times, use

```
linkedin > 10
```

`@pre_exercise_code`

```{r}
# no pec
```

`@sample_code`

```{r}
# The linkedin and facebook vectors have already been created for you
linkedin <- c(16, 9, 13, 5, 2, 17, 14)
facebook <- c(17, 7, 5, 16, 8, 13, 14)

# Popular days


# Quiet days


# LinkedIn more popular than Facebook

```

`@solution`

```{r}
# The linkedin and facebook vectors have already been created for you
linkedin <- c(16, 9, 13, 5, 2, 17, 14)
facebook <- c(17, 7, 5, 16, 8, 13, 14)

# Popular days
linkedin > 15

# Quiet days
linkedin <= 5

# LinkedIn more popular than Facebook
linkedin > facebook
```

`@sct`

```{r}
test_error()
msg <- "Do not remove or change the definition of the vectors `linkedin` and `facebook`!"
test_object("linkedin", undefined_msg = msg, incorrect_msg = msg)
test_object("facebook", undefined_msg = msg, incorrect_msg = msg)
test_output_contains("linkedin > 15", times = 1, incorrect_msg = "Check your code to find popular LinkedIn days. You can use `> 15` for this. Simply print the result.")
test_output_contains("linkedin <= 5", times = 1, incorrect_msg = "Check your code to find quiet LinkedIn days. You can use `<= 5` for this. Make sure to use the appropriate relational operator, and print the result.")
test_output_contains("linkedin > facebook", times = 1, incorrect_msg = "Have you correctly solved the last instruction? Simply combine `linkedin` and `facebook` with `>` so for each day you get `TRUE` or `FALSE`; `TRUE` if your LinkedIn profile had more visitors than your Facebook profile, `FALSE` otherwise. Simply print the result.")

success_msg("Wonderful! Have a look at the console output. Your LinkedIn profile was pretty popular on the sixth day, but less so on the fourth and fifth day.")
```

---

## Compare matrices


```yaml
type: NormalExercise
lang: r
xp: 100
skills: '1'
key: 3eb73a1959d23a93bc8224b488f50c6b3a1ecb5f
```


R's ability to deal with different data structures for comparisons does not stop at vectors. Matrices and relational operators also work together seamlessly!

Instead of in vectors (as in the previous exercise), the LinkedIn and Facebook data is now stored in a matrix called `views`. The first row contains the LinkedIn information; the second row the Facebook information. The original vectors `facebook` and `linkedin` are still available as well.

`@instructions`

Using the relational operators you've learned so far, try to discover the following:

- When were the views exactly equal to 13? Use the `views` matrix to return a logical matrix.
- For which days were the number of views less than or equal to 14? Again, have R return a logical matrix.

`@hint`

To see when `views` equals 13, you can use the `==` operator, just like you did for vectors!

`@pre_exercise_code`

```{r}
# no pec
```

`@sample_code`

```{r}
# The social data has been created for you
linkedin <- c(16, 9, 13, 5, 2, 17, 14)
facebook <- c(17, 7, 5, 16, 8, 13, 14)
views <- matrix(c(linkedin, facebook), nrow = 2, byrow = TRUE)

# When does views equal 13?


# When is views less than or equal to 14?

```

`@solution`

```{r}
# The social data has been created for you
linkedin <- c(16, 9, 13, 5, 2, 17, 14)
facebook <- c(17, 7, 5, 16, 8, 13, 14)
views <- matrix(c(linkedin, facebook), nrow = 2, byrow = TRUE)

# When does views equal 13?
views == 13

# When is views less than or equal to 14?
views <= 14
```

`@sct`

```{r}
test_error()
msg <- "Do not remove or change the definition of the predefined variables `linkedin`, `facebook` and `views`."
test_object("linkedin", undefined_msg = msg, incorrect_msg = msg)
test_object("facebook", undefined_msg = msg, incorrect_msg = msg)
test_object("views", undefined_msg = msg, incorrect_msg = msg)

test_output_contains("views == 13", incorrect_msg = "Have a second look at the code that calculates when the `views` matrix is equal to 13. You can use `views == 13`. Make sure to print the result.")
test_output_contains("views <= 14", incorrect_msg = "Have another look at the second instruction. Are you using the `<=` operator? Simply print the result, there's no need to assign it to a new variable.")

success_msg("Nice job! This exercise concludes the part on comparators. Now that you know how to query the relation between R objects, the next step will be to use the results to alter the behavior of your programs. Find out all about that in the next video!")
```

---

## Logical Operators



```yaml
type: VideoExercise
lang: r
xp: 50
skills: '1'
key: d796c57afad487554aa6475903f8f07be791d7a0
video_link: |
  //player.vimeo.com/video/160339465
video_hls: |+
  //videos.datacamp.com/transcoded/672_intermediate_r/v1/hls-ch1_2.master.m3u8

```


`@projector_key`
40d6a3d08d74610f01ccaca8ae8fdac1



---

## & and |


```yaml
type: NormalExercise
lang: r
xp: 100
skills: '1'
key: 2312858c6427900ac8a8ed6abc1287f54d7e4a59
```


Before you work your way through the next exercises, have a look at the following R expressions. All of them will evaluate to `TRUE`:

```
TRUE & TRUE
FALSE | TRUE
5 <= 5 & 2 < 3
3 < 4 | 7 < 6
```

Watch out: `3 < x < 7` to check if `x` is between 3 and 7 will not work; you'll need `3 < x & x < 7` for that.

In this exercise, you'll be working with the `last` variable. This variable equals the last value of the `linkedin` vector that you've worked with previously. The `linkedin` vector represents the number of LinkedIn views your profile had in the last seven days, remember? Both the variables `linkedin` and `last` have already been defined in the editor.

`@instructions`

Write R expressions to solve the following questions concerning the variable `last`:

- Is `last` under 5 or above 10?
- Is `last` between 15 and 20, excluding 15 but including 20?

`@hint`

In the last instruction, you should use the `&` operator twice and the `|` operator once. Use parentheses to make sure that the order of execution is correct!

`@pre_exercise_code`

```{r}
# no pec
```

`@sample_code`

```{r}
# The linkedin and last variable are already defined for you
linkedin <- c(16, 9, 13, 5, 2, 17, 14)
last <- tail(linkedin, 1)

# Is last under 5 or above 10?


# Is last between 15 (exclusive) and 20 (inclusive)?

```

`@solution`

```{r}
# The linkedin and last variable are already defined for you
linkedin <- c(16, 9, 13, 5, 2, 17, 14)
last <- tail(linkedin, 1)

# Is last under 5 or above 10?
last < 5 | last > 10

# Is last between 15 (exclusive) and 20 (inclusive)?
last > 15 & last <= 20
```

`@sct`

```{r}
test_error()
msg <- "Do not remove or change the code that create `linkedin` and `last`"
test_object("linkedin", undefined_msg = msg, incorrect_msg = msg)
test_object("last", undefined_msg = msg, incorrect_msg = msg)

msg <- "In your code for the %s instruction, you should use %s%s."
test_student_typed(strings = c("last < 5", "5 > last"), not_typed_msg = sprintf(msg, "first", "`last < 5`", ""))
test_student_typed(strings = c("last > 10", "last < 10"), not_typed_msg = sprintf(msg, "first", "`last > 10`", ""))
test_student_typed(strings = c("|", "||"), not_typed_msg = sprintf(msg, "first", "the or operator (`|`)", ", to combine `last < 5` and `last > 10`"))

test_student_typed(strings = c("last > 15", "15 < last"), not_typed_msg = sprintf(msg, "second", "`last > 15`", ""))
test_student_typed(strings = c("last <= 20", "20 >= last"), not_typed_msg = sprintf(msg, "second", "`last <= 20`", ""))
test_student_typed(strings = c("&", "&&"), not_typed_msg = sprintf(msg, "second", "the and operator (`&`)", ", to combine `last > 15` and `last <= 20`"))

success_msg("Great! Have one last look at the console before proceeding; do the results of the different expressions make sense?")
```

---

## & and | (2)


```yaml
type: NormalExercise
lang: r
xp: 100
skills: '1'
key: f0aaad24a6cccb5004016b07d4ac45a151816a4b
```


Like relational operators, logical operators work perfectly fine with vectors and matrices.

Both the vectors `linkedin` and `facebook` are available again. Also a matrix - `views` - has been defined; its first and second row correspond to the `linkedin` and `facebook` vectors, respectively. Ready for some advanced queries to gain more insights into your social outreach?

`@instructions`

- When did LinkedIn views exceed 10 _and_ did Facebook views fail to reach 10 for a particular day? Use the `linkedin` and `facebook` vectors.
- When were one or both of your LinkedIn and Facebook profiles visited at least 12 times?
- When is the `views` matrix equal to a number between 11 and 14, excluding 11 and including 14?

`@hint`

Be sure to using a single `&` and a single `|` in these exercises! `&&` and `||` will only examine the first element of your vector or matrix.

`@pre_exercise_code`

```{r}
# no pec
linkedin <- c(16, 9, 13, 5, 2, 17, 14)
facebook <- c(17, 7, 5, 16, 8, 13, 14)
views <- matrix(c(linkedin, facebook), nrow = 2, byrow = TRUE)
```

`@sample_code`

```{r}
# The social data (linkedin, facebook, views) has been created for you

# linkedin exceeds 10 but facebook below 10


# When were one or both visited at least 12 times?


# When is views between 11 (exclusive) and 14 (inclusive)?

```

`@solution`

```{r}
# The social data (linkedin, facebook, views) has been created for you

# linkedin exceeds 10 but facebook below 10
linkedin > 10 & facebook < 10

# When were one or both visited at least 12 times?
linkedin >= 12 | facebook >= 12

# When is views between 11 (exclusive) and 14 (inclusive)?
views > 11 & views <= 14
```

`@sct`

```{r}
test_error()
msg <- "Do not remove or change the definition of the predefined variables `linkedin`, `facebook` and `views`."
test_object("linkedin", undefined_msg = msg, incorrect_msg = msg)
test_object("facebook", undefined_msg = msg, incorrect_msg = msg)
test_object("views", undefined_msg = msg, incorrect_msg = msg)

msg <- "In your code for the %s instruction, you should use `%s`."

test_student_typed(strings = c("linkedin > 10", "10 < linkedin"), not_typed_msg = sprintf(msg, "first", "linkedin > 10"))
test_student_typed(strings = c("facebook < 10", "10 > facebook"), not_typed_msg = sprintf(msg, "first", "facebook < 10"))
test_output_contains("linkedin > 10 & facebook < 10", incorrect_msg = "Have another look at your solution for the first instruction. Make sure to use `&`. Print out the result.")

test_student_typed(strings = c("linkedin >= 12", "12 <= linkedin"), not_typed_msg = sprintf(msg, "second", "linkedin >= 12"))
test_student_typed(strings = c("facebook >= 12", "12 <= facebook"), not_typed_msg = sprintf(msg, "second", "facebook >= 12"))
test_output_contains("linkedin >= 12 | facebook >= 12", incorrect_msg = "Have another look at your code for the second instruction. Make sure to use the correct logical operator: `|`.")

test_student_typed(strings = c("views > 11", "11 < views"), not_typed_msg = sprintf(msg, "third", "views > 11"))
test_student_typed(strings = c("views <= 14", "14 >= views"), not_typed_msg = sprintf(msg, "third", "views <= 14"))
test_output_contains("views > 11 & views <= 14", incorrect_msg = "Your code for the final instruction is not correct. Make sure to use the `&` operator.")

success_msg("Bravo! You'll have noticed how easy it is to use logical operators to vectors and matrices. What do these results tell us? The third day of the recordings was the only day where your LinkedIn profile was visited more than 10 times, while your Facebook profile wasn't. Can you draw similar conclusions for the other results?")
```

---

## Reverse the result: !


```yaml
type: PureMultipleChoiceExercise
lang: r
xp: 50
skills: '1'
key: 12d2fadddf9091b8dd35ae0ca402d7f7a767e1e8
```


On top of the `&` and `|` operators, you also learned about the `!` operator, which negates a logical value. To refresh your memory, here are some R expressions that use `!`. They all evaluate to `FALSE`:

```
!TRUE
!(5 > 3)
!!FALSE
```

What would the following set of R expressions return?

```
x <- 5
y <- 7
!(!(x < 4) & !!!(y > 12))
```

`@possible_answers`

- `TRUE`
- [`FALSE`]
- Running this piece of code would throw an error.

`@hint`

- Parentheses enforce a particular order of execution. For example `2 + 3 * 5` equals `17`, while `(2 + 3) * 5` equals 25.
- `!!!x` corresponds to `!x`.


`@feedback`

- Incorrect, try again. If you're not sure, you can simply copy the code to the console, run it and inspect the result.
- Great!
- Incorrect, try again. There's nothing wrong with this code. Using a triple negation - `!!!` - is not very useful, but it is syntactically correct.

---

## Blend it all together


```yaml
type: NormalExercise
lang: r
xp: 200
skills: '1'
key: a465bb6fe887f70bfdc19380672ed23f8549b06f
```


With the things you've learned by now, you're able to solve pretty cool problems.

Instead of recording the number of views for your own LinkedIn profile, suppose you conducted a survey inside the company you're working for. You've asked every employee with a LinkedIn profile how many visits their profile has had over the past seven days. You stored the results in a data frame called `li_df`. This data frame is available in the workspace; type `li_df` in the console to check it out.

`@instructions`

- Select the entire second column, named `day2`, from the `li_df` data frame as a vector and assign it to `second`.
- Use `second` to create a logical vector, that contains `TRUE` if the corresponding number of views is strictly greater than 25 or strictly lower than 5 and `FALSE` otherwise. Store this logical vector as `extremes`.
- Use `sum()` on the `extremes` vector to calculate the number of `TRUE`s in `extremes` (i.e. to calculate the number of employees that are either very popular or very low-profile). Simply print this number to the console.

`@hint`

- You can select the data for the second day with `li_df$day2`.
- Use a combination of relational and logical operators for the second instruction: `>`, `<` and `|`.
- `sum(extremes)` will count all the `TRUE`s in `extremes`.

`@pre_exercise_code`

```{r}
set.seed(1234)
views <- runif(50)*35
li_df <- data.frame(views,views,views,views,views,views,views)
rm(views)
names(li_df) <- paste0(rep("day",7),1:7)
li_df <- as.data.frame(lapply(li_df, function(x) abs(round(jitter(x, amount = 7)))))
li_df[li_df == 16] = 17
rownames(li_df) <- paste0(rep("employee_",nrow(li_df)), 1:nrow(li_df))
```

`@sample_code`

```{r}
# li_df is pre-loaded in your workspace

# Select the second column, named day2, from li_df: second


# Build a logical vector, TRUE if value in second is extreme: extremes


# Count the number of TRUEs in extremes


# Solve it with a one-liner

```

`@solution`

```{r}
# li_df is pre-loaded in your workspace

# Select the second column, named day2, from li_df: second
second <- li_df$day2

# Build a logical vector, TRUE if value in second is extreme: extremes
extremes <- second > 25 | second < 5

# Count the number of TRUEs in extremes
sum(extremes)

# Solve it with a one-liner
sum(li_df$day2 > 25 | li_df$day2 < 5)
```

`@sct`

```{r}
test_correct({
  test_output_contains("sum(li_df$day2 > 25 | li_df$day2 < 5)", incorrect_msg = "Have you correctly used `sum()` to print out the number of extreme views?")
}, {
  test_object("second", incorrect_msg = "Have you correctly defined `second`? You can use `li_df$day2`")
  test_object("extremes", incorrect_msg = "Have you correctly built extremes? You should combine `second > 25` and `second < 5` with the `|` operator.")
})
success_msg("Great! Head over to the next video and learn how relational and logical operators can be used to alter the flow of your R scripts.")
```

---

## Conditional Statements



```yaml
type: VideoExercise
lang: r
xp: 50
skills: '1'
key: efe188f1d925e85aef1bfae5276b0992b63bac71
video_link: |
  //player.vimeo.com/video/160339462
video_hls: |
  //videos.datacamp.com/transcoded/672_intermediate_r/v1/hls-ch1_3.master.m3u8
```


`@projector_key`
2fc249b0f2d184de0feef4e633c49bad



---

## The if statement


```yaml
type: NormalExercise
lang: r
xp: 100
skills: '1'
key: d918315c5026a542544fb9577b4cda99dcb31cef
```


Before diving into some exercises on the `if` statement, have another look at its syntax:

```
if (condition) {
  expr
}
```

Remember your vectors with social profile views? Let's look at it from another angle. The `medium` variable gives information about the social website; the `num_views` variable denotes the actual number of views that particular `medium` had on the last day of your recordings. Both these variables have already been defined in the editor.

`@instructions`

- Examine the `if` statement that prints out "Showing LinkedIn information" if the `medium` variable equals "LinkedIn".
- Code an `if` statement that prints "You're popular!" to the console if the `num_views` variable exceeds 15.

`@hint`

Use the [`print()`](http://www.rdocumentation.org/packages/base/functions/print) function to print things to the console output. Have another look at the video if you are not sure how to write your own if statements.

`@pre_exercise_code`

```{r}
# no pec
```

`@sample_code`

```{r}
# Variables related to your last day of recordings
medium <- "LinkedIn"
num_views <- 14

# Examine the if statement for medium
if (medium == "LinkedIn") {
  print("Showing LinkedIn information")
}

# Write the if statement for num_views



```

`@solution`

```{r}
# Variables related to your last day of recordings
medium <- "LinkedIn"
num_views <- 14

# Examine the if statement for medium
if (medium == "LinkedIn") {
  print("Showing LinkedIn information")
}

# Write the if statement for num_views
if (num_views > 15) {
  print("You're popular!")
}
```

`@sct`

```{r}
test_error()

test_if_else(index = 2,
             if_cond_test = {
               test_student_typed(c("num_views > 15", "15 < num_views"),
                                  not_typed_msg = "Have another look at the `condition` part of your second `if` statement. You can use `num_views > 15`, for example.")
             },
             if_expr_test = {
               msg <- "Inside the body of your `if` statement, use the function `print()` to print the message `\"You're popular!\"` when the number of views exceeds 15. Remember that R is case sensitive."
               test_function("print", "x", not_called_msg = msg, incorrect_msg = msg)
             })

success_msg("Great! Try to see what happens if you change the `medium` and `num_views` variables and run your code again. Let's further customize these if statements in the next exercise.")
```

---

## Add an else


```yaml
type: NormalExercise
lang: r
xp: 100
skills: '1'
key: 612175344bc2ba187a764bce0cadc6a3ac4b5a95
```


You can only use an `else` statement in combination with an `if` statement. The `else` statement does not require a condition; its corresponding code is simply run if all of the preceding conditions in the control structure are `FALSE`. Here's a recipe for its usage:

```
if (condition) {
  expr1
} else {
  expr2
}
```

_It's important that the `else` keyword comes on the same line as the closing bracket of the `if` part!_

Both `if` statements that you coded in the previous exercises are already available in the editor. It's now up to you to extend them with the appropriate `else` statements!

`@instructions`

Add an `else` statement to both control structures, such that

- "Unknown medium" gets printed out to the console when the if-condition on `medium` does not hold.
- R prints out "Try to be more visible!" when the if-condition on `num_views` is not met.

`@hint`

To add an else statement, change:

```
if (___) {
  ___
}
```
to

```
if (___) {
  ___
} else {
  ___
}
```

Up to you to fill in the `___`!

`@pre_exercise_code`

```{r}
# no pec
```

`@sample_code`

```{r}
# Variables related to your last day of recordings
medium <- "LinkedIn"
num_views <- 14

# Control structure for medium
if (medium == "LinkedIn") {
  print("Showing LinkedIn information")
}



# Control structure for num_views
if (num_views > 15) {
  print("You're popular!")
}
```

`@solution`

```{r}
# Variables related to your last day of recordings
medium <- "LinkedIn"
num_views <- 14

# Control structure for medium
if (medium == "LinkedIn") {
  print("Showing LinkedIn information")
} else {
  print("Unknown medium")
}

# Control structure for num_views
if (num_views > 15) {
  print("You're popular!")
} else {
  print("Try to be more visible!")
}
```

`@sct`

```{r}
test_error()
test_if_else(index = 1,
             if_cond_test = {
               test_student_typed(c("medium == \"LinkedIn\"", "\"LinkedIn\" == medium"),
                                  not_typed_msg = "Have another look at the `condition` part of the first control structure. It was already coded for you!")
             },
            if_expr_test = {
              msg <- "Don't change anything about the printout of the message in the `if` part of the first control structure. It has already been coded for you!"
              test_function("print", "x", not_called_msg = msg, incorrect_msg = msg)
            },
            else_expr_test = {
              msg <- "In the `else` part of the first control construct, make sure to print `\"Unknown medium\"` using the `print()` function. R is case sensitive!"
              test_function("print", "x", not_called_msg = msg, incorrect_msg = msg)
            })

test_if_else(index = 2,
             if_cond_test = {
               test_student_typed(c("num_views > 15", "15 < num_views"),
                                  not_typed_msg = "The `condition` part of the second control structure is already coded for you; don't change it.")
             },
             if_expr_test = {
               msg <- paste("Use the function `print()` to print the message `\"You're popular!\"`",
                            "when the number of views exceeds 15. It was already coded for you!")
               test_function("print", "x", not_called_msg = msg, incorrect_msg = msg)
             },
             else_expr_test = {
               msg <- "In the `else` part of the second control construct, make sure to print `\"Try to be more visible!\"` using the `print()` function."
              test_function("print", "x", not_called_msg = msg, incorrect_msg = msg)
             })

success_msg("Great job! You also had Facebook information available, remember? Time to add some more statements to our control structures using `else if`!")
```

---

## Customize further: else if


```yaml
type: NormalExercise
lang: r
xp: 100
skills: '1'
key: 3cee6fde800c62e0d36e0558a666946f513d022b
```


The `else if` statement allows you to further customize your control structure. You can add as many `else if` statements as you like. Keep in mind that R ignores the remainder of the control structure once a condition has been found that is `TRUE` and the corresponding expressions have been executed. Here's an overview of the syntax to freshen your memory:

```
if (condition1) {
  expr1
} else if (condition2) {
  expr2
} else if (condition3) {
  expr3
} else {
  expr4
}
```

_Again, It's important that the `else if` keywords comes on the same line as the closing bracket of the previous part of the control construct!_

`@instructions`

Add code to both control structures such that:

- R prints out "Showing Facebook information" if `medium` is equal to "Facebook". Remember that R is case sensitive!
- "Your number of views is average" is printed if `num_views` is between 15 (inclusive) and 10 (exclusive).
Feel free to change the variables `medium` and `num_views` to see how the control structure respond. In both cases, the existing code should be extended in the `else if` statement. No existing code should be modified.

`@hint`

For both instructions, just keep the `if`, `else if` and `else` statements that are already available; just add the appropriate code within the `else if` statement.

`@pre_exercise_code`

```{r}
# no pec
```

`@sample_code`

```{r}
# Variables related to your last day of recordings
medium <- "LinkedIn"
num_views <- 14

# Control structure for medium
if (medium == "LinkedIn") {
  print("Showing LinkedIn information")
} else if (medium == "Facebook") {
  # Add code to print correct string when condition is TRUE

} else {
  print("Unknown medium")
}

# Control structure for num_views
if (num_views > 15) {
  print("You're popular!")
} else if (num_views <= 15 & num_views > 10) {
  # Add code to print correct string when condition is TRUE

} else {
  print("Try to be more visible!")
}
```

`@solution`

```{r}
# Variables related to your last day of recordings
medium <- "LinkedIn"
num_views <- 14

# Control structure for medium
if (medium == "LinkedIn") {
  print("Showing LinkedIn information")
} else if (medium == "Facebook") {
  # Add code to print correct string when condition is TRUE
  print("Showing Facebook information")
} else {
  print("Unknown medium")
}

# Control structure for num_views
if (num_views > 15) {
  print("You're popular!")
} else if (num_views <= 15 & num_views > 10) {
  # Add code to print correct string when condition is TRUE
  print("Your number of views is average")
} else {
  print("Try to be more visible!")
}
```

`@sct`

```{r}
rst_btn <- "You can reset to the predefined code by using the button in the lower right corner of your script editor window."
test_error()
test_if_else(index = 1,
             if_cond_test = {
               test_student_typed(c("medium == \"LinkedIn\"", "\"LinkedIn\" == medium"),
                                  not_typed_msg = paste("Don't change anything about the `if` part of the first control structure,",
                                                        "it has already been coded for you.", rst_btn))
             },
             if_expr_test = {
                msg <- paste("Don't change anything about the `if` part of the first control structure,",
                             "it has already been coded for you.", rst_btn)
                test_function("print", "x", not_called_msg = msg, incorrect_msg = msg)
             },
             else_expr_test = {
                test_if_else(index = 1,
                             if_cond_test = {
                               test_student_typed(c("medium == \"Facebook\"", "\"Facebook\" == medium"),
                                                  not_typed_msg = paste("Make sure to code the correct condition for the `else if`",
                                                                        "part of the first control structure. It was already coded for you.", rst_btn))
                               },
                             if_expr_test = {
                               msg <- paste("In the `else if` part of the first control construct, make sure to print",
                                            "`\"Showing Facebook information\"` using the `print()` function.")
                               test_function("print", "x", not_called_msg = msg, incorrect_msg = msg)
                              },
                              else_expr_test = {
                                msg <- paste("Don't change anything about the `else` part of the first control structure.",
                                             "It was coded for you.",
                                             rst_btn)
                                test_function("print", "x", not_called_msg = msg, incorrect_msg = msg)
                            },
                            not_found_msg = paste("Don't remove the `else if` chunk at the appropriate location in the first control structure. You should add code to it.", rst_btn)
             )})

test_if_else(index = 2,
             if_cond_test = {
               test_student_typed(c("num_views > 15", "15 < num_views"),
                                  not_typed_msg = paste("The condition part of the `if` statement in the second control structure is already coded for you;",
                                                        "don't change it.",rst_btn))
             },
             if_expr_test = {
                msg <- paste("Use the function `print()` to print the message `\"You're popular!\"`",
                            "when the number of views exceeds 15. It was already coded for you!", rst_btn)
                test_function("print", "x", not_called_msg = msg, incorrect_msg = msg)
             },
             else_expr_test = {
                test_if_else(index = 1,
                             if_cond_test = {
                               test_student_typed(c("num_views > 10", "10 < num_views"),
                                                  not_typed_msg = paste("Make sure to code the correct condition for the `else if`",
                                                                        "part of the second control structure. It was already coded for you.", rst_btn))
                               },
                             if_expr_test = {
                               msg <- paste("In the `else if` part of the second control construct, make sure to print",
                                            "`\"Your number of views is average\"` using the `print()` function.")
                               test_function("print", "x", not_called_msg = msg, incorrect_msg = msg)
                              },
                              else_expr_test = {
                                msg <- paste("Don't change anything about the `else` part of the second control structure.",
                                             "It was coded for you.",
                                             rst_btn)
                                test_function("print", "x", not_called_msg = msg, incorrect_msg = msg)
                            },
                            not_found_msg = paste("Don't remove the `else if` chunk at the appropriate location in the second control structure. You should add code to it.", rst_btn)
                )
             })

success_msg("Awesome! Have another look at the second control structure. Because R abandons the control flow as soon as it finds a condition that is met, you can simplify the condition for the `else if` part in the second construct to `num_views > 10`.")
```

---

## Else if 2.0


```yaml
type: MultipleChoiceExercise
lang: r
xp: 50
skills: '1'
key: 8556f5db89566259de0dc8ae3532b1cde05956c4
```


You can do anything you want inside if-else constructs. You can even put in another set of conditional statements. Examine the following code chunk:

```
if (number < 10) {
  if (number < 5) {
    result <- "extra small"
  } else {
    result <- "small"
  }
} else if (number < 100) {
  result <- "medium"
} else {
  result <- "large"
}
print(result)
```

Have a look at the following statements:

1. If `number` is set to 6, "small" gets printed to the console.
2. If `number` is set to 100, R prints out "medium".
3. If `number` is set to 4, "extra small" gets printed out to the console.
4. If `number` is set to 2500, R will generate an error, as `result` will not be defined.

Select the option that lists <u>all</u> the true statements.

`@instructions`

- 2 and 4
- 1 and 4
- 1 and 3
- 2 and 3

`@hint`

If you're doubting whether a statement is valid, you can simply define the variable `number` yourself in the console and run the code chunk afterwards.

`@pre_exercise_code`

```{r}
# no pec
```

`@sct`

```{r}
msg1 = "The condition related to the `else if` statement does not include 100, so the second statement is false. Try again."
msg2 = "If `number` is equal to 2500, R will simply run the expressions related to the final `else` statement. Have another look"
msg3 = "Wonderful! If you got this one right, the next exercise will be a piece of cake."
msg4 = msg2
test_mc(correct = 3, feedback_msgs = c(msg1, msg2, msg3, msg4))
```

---

## Take control!


```yaml
type: NormalExercise
lang: r
xp: 100
skills: '1'
key: 3033381d0fe81241dc5957389ef08c39642f3f42
```


In this exercise, you will combine everything that you've learned so far: relational operators, logical operators and control constructs. You'll need it all!

In the editor, we've coded two values beforehand: `li` and `fb`, denoting the number of profile views your LinkedIn and Facebook profile had on the last day of recordings. Go through the instructions to create R code that generates a 'social media score', `sms`, based on the values of `li` and `fb`.

`@instructions`

Finish the control-flow construct with the following behavior:

- If both `li` and `fb` are 15 or higher, set `sms` equal to double the sum of `li` and `fb`.
- If both `li` and `fb` are strictly below 10, set `sms` equal to half the sum of `li` and `fb`.
- In all other cases, set `sms` equal to `li + fb`.
- Finally, print the resulting `sms` variable to the console.

`@hint`

There are several ways to solve this exercise. The easiest will be to use an `if`-`else if`-`else` construct, and maintain the order of the instructions in your construct. You'll need the `&` operator in this approach.

`@pre_exercise_code`

```{r}
# no pec
```

`@sample_code`

```{r}
# Variables related to your last day of recordings
li <- 15
fb <- 9

# Code the control-flow construct
if (___ & ___) {
  sms <- 2 * (li + fb)
} ___ (___) {
  sms <- 0.5 * (li + fb)
} else {
  sms <- ___
}

# Print the resulting sms to the console

```

`@solution`

```{r}
# Variables related to your last day of recordings
li <- 15
fb <- 9

# Code the control-flow construct
if (li >= 15 & fb >= 15) {
  sms <- 2 * (li + fb)
} else if (li < 10 & fb < 10) {
  sms <- 0.5 * (li + fb)
} else {
  sms <- li + fb
}

# Print the resulting sms to the console
sms
```

`@sct`

```{r}
test_error()
msg <- "Feel free to experiment with different values of `li` and `fb` when you're working on a solution, but set them to `15` and `9` before your final submission!"
test_object("li", undefined_msg = msg, incorrect_msg = msg)
test_object("fb", undefined_msg = msg, incorrect_msg = msg)

test_correct({
  test_object("sms", incorrect_msg = "There's still something wrong with your code, because `sms` isn't correct. Have another look at your control structure.")
}, {
  test_if_else(index = 1,
               if_cond_test = {
                 test_student_typed(c("li >= 15", "15 <= li"), not_typed_msg = "You should use `li >= 15` or something equivalent in the `if` condition.")
                 test_student_typed(c("fb >= 15", "15 <= fb"), not_typed_msg = "You should use `fb >= 15` or something equivalent in the `if` condition.")
                 test_student_typed(c("&"), not_typed_msg = "Make sure to use an `&` to combine the conditions inside the if statement.")
               },
               else_expr_test = {
                 test_if_else(index = 1,
                              not_found_msg = "Have you added an `if else` statement to the control flow construct?",
                              if_cond_test = {
                                test_student_typed(c("li < 10", "10 > li"), not_typed_msg = "You should use `li < 10` or something equivalent in the `else if` condition.")
                                test_student_typed(c("fb < 10", "10 > fb"), not_typed_msg = "You should use `fb < 10` or something equivalent in the `else if` condition.")
                                test_student_typed(c("&"), not_typed_msg = "Make sure to use an `&` to combine the conditions inside the `else if` statement.")
                              },
                              if_expr_test = {
                                test_student_typed("sms <- 0.5 * (li + fb)", not_typed_msg = "Don't change the code to calculate `sms` in the `else if` case: `sms <- 0.5 * (li + fb)`")
                              },
                              else_expr_test = {
                                test_student_typed(c("li + fb", "fb + li"), not_typed_msg = "Use `li + fb` or something equivalent to create `sms` in the `else` case.")
                              })
               })
})


test_output_contains("sms", incorrect_msg = "Don't forget to print the resulting `sms`!")
success_msg("Bellissimo! Feel free to play around some more with your solution by changing the values of `li` and `fb`.")
```
