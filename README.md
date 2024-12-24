# Blackjack Game 🃏

A simple console-based Blackjack game written in Python.

## Features ✨
- Standard gameplay rules 📝.
- Player can choose to (H)it or (S)tand ✋.
- Dealer hits until they reach 17 or higher 💳.
- The game supports multiple rounds until the player chooses to quit 🔁.
- Cards are randomly shuffled for each round 🔄.
- **Balance management**: The player’s balance is tracked, and they can continue playing as long as they have enough funds (minimum bet of 5$) 💸.
- **Bust Handling**: The game continues even if the player busts, as long as they have enough balance to place another bet 🔄.
- Proper handling when the player gets 21 🏆.

## Updates ✅
- (24.12) Made proper handling when player has 21 🎉.
- (24.12) Fixed bugs with double printing in the console 🔧.
- (24.12) Fixed bug with multiple printing of player and dealer hands 🛠️.

## How to Play 🎮
1. When prompted, enter `(D)` to start a new round or `(Q)` to quit the game ✋❌.
2. The game will deal cards to both the player 🧑‍🦱 and the dealer 🧑‍💼. The dealer’s second card will be hidden initially 🕵️‍♂️.
3. As the player, you can choose to (H)it to take another card or (S)tand to end your turn ⬆️➡️.
4. The dealer will automatically continue drawing cards until their total is 17 or more 🃏➡️.
5. The winner is determined based on who has the higher hand value without exceeding 21 🏆. If both the player and dealer have the same value, it’s a tie ("Push") 🤝.
6. If you bust, you can still continue playing in the next round if your balance allows it 🔄.

## To Do 🛠️
- **Make the console printing better**: Enhance the formatting for readability 🖥️.
- **Add split function**: Only when the player receives pairs or cards with the same value 🔀.
- **Add double down function**: Let the player double their bet after receiving the first two cards 💰.
- **Insurance check**: Add a feature to check if the player wants to place an insurance bet 🛡️.
- **UI**: Improve the user interface (UI) for better experience 🎨.

## Bugs to Fix 🐞
- If the dealer has 21, it cancels the game on the first deal, even though the second card is hidden and the value is not displayed to the player.
