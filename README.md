 ## Project Name
 - Password Locker

 ## Author 
 - Catherine Nduku

 ## Description 
  - This project enables a user to store old accounts credentials and create new ones. the program also stores. Users get the option to come up with their own passwords or the program can generate one for them. the program further displays the user accounts and passwords upon being prompted.

  ## BDD 
  These are the behaviours/features that the application implements for use by a user.

As a user I would like:
* To create an account with my details - log in and password
* Store my existing login credentials
* Generate a password for a new credential/account
* Copy my credentials to the clipboard

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display codes for navigation | **In terminal: $./password_locker.py** | Welcome, choose an option: ca-Create Account, li-Log In, ex-Exit |
| Display prompt for creating an account | **Enter: ca** | Enter your first name, last name and password |
| Display prompt for login in | **Enter: li** | Enter your account name and password |
| Display codes for navigation | **Successful login** | Choose an option: cc - Create Credential, dc - Display Credentials, copy - Copy Credential, ex - exit |
| Display prompt for creating a credential | **Enter: cc** | Enter the site name, your username and password |
| Display a list of credentials | **Enter: dc** | Prints a list of saved credentials |
| Display prompt for which credential to copy | **Enter: copy** | Enter the site name of the credential you wish to copy. |
| Exit application | **Enter: ex** | Exit the current navigation stage |


## Technologies used
- Python3.6

## SetUp / Installation Requirements

* python3.6
* Good internet connection
*  For windows users:  GitBash
* For linux/ubuntu users : Git

### Cloning
* In your terminal:
        
        $ git clone https://github.com/catherine244/Password-Locker.git
        $ cd Python-Password-Locker

## Running the Application
* To run the application, in your terminal:

        $ ./run.py
      
        
## Testing the Application
* To run the tests for the class file and check if it functions well:

        $ python3.6 credentials_test.py
        
## Contacts 
  ccayreen24@gmail.com

  ## License 
  [MIT License](https://github.com/catherine244/Password-Locker//blob/master/LICENSE) [Catherine](https://github.com/catherine244). 


