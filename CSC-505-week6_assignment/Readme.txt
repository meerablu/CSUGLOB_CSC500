Requirements for App:
1) Basic interpreter for Python is required to run the program. 

Specifications/Requirements/Design for Checkwriter app - 
1) Writes a single check per session with the user (the payor name serves as signatory)
2) Handles only basic check writing with fields such as Date, Signature, Payee and Amount dollar and cents.
3) Value check input validations are in place. 
4) Translates dollar value into phrasal value in dollars and cents (main function). Example $23.21 is Twenty three dollars and twenty one cents.

Constraints and Limitations for Checkwriter app-
1) Handles check amounts up to 7 digit (Million range only) - this is below $10 Mil.
2) Comma separators in dollar value is not added. Only $123234.21  as an example without the , .
3) Does not generate a physical copy of the check written.
4) Confirmation/controls to confirm check information is not fully implemented.
5) Testing has not been fully executed - subject to small bugs.
