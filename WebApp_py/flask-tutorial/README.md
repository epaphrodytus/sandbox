# Flask Tutorial

| Useful References                                                                                 |
| ------------------------------------------------------------------------------------------------- |
| [Flask Tutorial Project Link](https://flask.palletsprojects.com/en/3.0.x/tutorial/)               |
| ['click' module documentation](https://click.palletsprojects.com/en/8.1.x/)                       |
| [Packaing Python Projects](#https://packaging.python.org/en/latest/tutorials/packaging-projects/) |

| Terms/Objects | Definitions                                                                                                                                                                      |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| View Function | Code you write to respond to requests to your applications                                                                                                                       |
| Blueprint     | A way to organize a group of related views and other code, acts as a sort of proxy between the applications and the views/code                                                   |
| Session       | Stores data across requests, data is stored in a _cookie_ that is sent to the browser                                                                                            |
| g             | You may think of this as a context object at the application level can be used to store information that needs to be accessible everywhere, automatically available in templates |
| request       | flask submodule that handles requests, automatiaclly available in templates                                                                                                      |
