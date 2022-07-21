# Python Challenge
<hr>

## Challenge 1

## Kid in a Candy Store
​
In this activity, you are creating the code a candy store will use in their state of the art candy vending machine!
​
### Instructions
​
* Create a loop that prints all of the candies in the store to the terminal with their index stored in brackets beside them.
​
  * For example: `"[0] Snickers"`
​
* Create a second loop that runs for a set number of times as determined by the variable `allowance`.
​
  * For example: If allowance is equal to five, the loop should run five times.
​
  * Each time this loop runs, take in a user's input - preferably a number - and then add the candy with a matching index to the variable `candy_cart`.
​
  * For example: If the user enters "0" as their input, "Snickers" should be added into the `candy_cart` list.
​
* Create a final loop to print all of the candies selected to the terminal.
​
### Bonus
​
* Create a version of the same code which allows a user to select as much candy as they want up until they say they do not want any more.

## Challenge 4
# Netflix lookup

Finding the info to some of Netflix's most popular videos

## Instructions

* Prompt the user for what video they are looking for.

* Search through the `netflix_ratings.csv` to find the user's video.

* If the CSV contains the user's video then print out the title, what it is rated and the current user ratings.

  * For example `"Pup Star is rated G with a rating of 82"`.

* If the CSV does not contain the user's video then print out a message telling them that their video could not be found.

**Bonus:**

* You may have noticed that there is more than one listing for some videos.

* Edit your code to have the title, the rating and user rating printed out only once.

* Set a variable to `False` to check if we found the video.

* In the `for loop` change the variable to confirm that the video is found.

* Insert a `break` statement into the `for loop` to stop the loop when the **first** movie is found. See the [documentation](https://docs.python.org/3.6/reference/simple_stmts.html#break) for additional info.

* If the CSV does not contain the user's video then print out a message telling them that their video could not be found.

Data Source: [Netflix Rating Data](http://theconceptcenter.com/simple-research-study-netflix-shows-analysis/)