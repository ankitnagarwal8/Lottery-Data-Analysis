This project seems to be about analyzing lottery data, specifically for the "Lotto 6/49" in Canada, and determining the probabilities of winning based on certain combinations of numbers. Here's an outline of the project:

Loading Lottery Data: The notebook begins by loading a dataset (649.csv) which presumably contains historical lottery results for the Lotto 6/49.

Extracting Winning Numbers:

A function extract_numbers is defined to extract the set of winning numbers from each row of the dataset.
It applies this function to the dataset to get the winning numbers.
Probability Calculations:

A function combinations is defined to calculate combinations (n choose k), which is important in determining the odds of matching a certain number of winning numbers.
Another function factorial is used to assist in this calculation.
Chances of Winning:

The notebook runs tests to calculate the probability of matching 2, 3, 4, or 5 numbers out of the total set, displaying the chances in percentage form and as fractions (e.g., "1 in 57 chances to win").
Output:

The notebook provides the probability of hitting 2 to 5 winning numbers, showing the output in both percentages and as odds (e.g., "1 in 1,032 chances").
Purpose:
The project aims to calculate the probabilities of winning in Lotto 6/49 based on historical data and mathematical modeling (combinatorics).

If you'd like to update this project for GitHub, I can help with any specific improvements, such as cleaning up the code, adding documentation, or writing a README file. How would you like to proceed with updating it?
