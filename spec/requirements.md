# Application for learning foreign languages #
Application should start with basic main menu with two buttons
- Strict dictionary drill
- Strict dictionary test
Example mockup is in file main-menu.png

Application should load example input json files like sample-input.json. The file contains list of question-answer items. The goal is to present each key (question) and wait for user input and then compare with expected value (answer). The user is notified whether or not the answer was correct or not.

## Strict dictionary drill ##
There should be a window that loads a sample json file and displays the following things:
- mode: LEARN
- file name
- total number of questions to be asked named "Total"
- number of learned words that is measured as number of correctly answered values named "Learned"
- number of questions left to be asked named "Left"
- Info "Press ESC to exit"
- Textbox with label "Question", it should be readonly
- Textbox with label "Answer", this is the place where user enters the answer

Questions are asked in random order. If the user correctly answers the question then this question will not be asked again in this session. If the answer was not provided correctly then it will be asked again until the correct answer is provided.

## Strict dictionary test ##
Looks the same as "Strict dictionary drill" with notable differences:
- mode: TEST (instead of LEARN)
- instead of "Learned" counter there is "Answered" counter which counts number of correctly answered questions

Questions are asked in random order. Each question is asked exactly once.

## Mockups ##
Example mockups that are relevant for "Strict dictionary drill" and "Strict dictionary test" are in files:
- drill-window.png
- drill-window-after-correct-answer.png
- drill-window-after-incorrect-answer.png

## Result ##
After "Strict dictionary drill" or "Strict dictionary test" ends there is a summary window displayed with user statistics within this session. Example mockup is in result-after-drill.png