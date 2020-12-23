PR: https://github.com/batoolmalkawii/automation/pull/1

# Automation

In this project, we analyzed a document `potential-contacts`, we used `regex` to find and collect all email addresses and phone numbers.

Once emails and phone numbers are found they are be stored in two separate documents. `emails.txt`, `phone_numbers.txt`.


Accepted Phone numbers are in various formats: 

    * (xxx) yyy-zzzz, yyy-zzzz, xxx-yyy-zzzz, etc.

    * phone numbers with missing area code should presume 206

    * phone numbers should be stored in xxx-yyy-zzzz format.

    * The information are sorted in ascending order.

> `phone_numbers.txt`
```
    123-456-7890
    206-678-9012
    234-567-8901
```
> `emails.txt`
```
ana@foo.bar
bill_x@foo.bar
chris.schmidt@bar.baz
```

# User Acceptance Tests:

Test Cases:

    1. Can successfully return emails in the correct format.

    2 Can successfully return phone numbers in the correct format.