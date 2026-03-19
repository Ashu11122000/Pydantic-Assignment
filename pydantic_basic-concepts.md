## Overview

→ Pydantic = Data Validation + Data Parsing (conversion)

→ Data Validation = Process of ensuring data is clean, correct, and useful before it is processed, stored, or analyzed.

→ Data Parsing = Process of analyzing breaking down and converting the raw, unstructured data into a readable format (like JSON), that software can easily understand.

→ Pydantic is like a smart gatekeeper
  * we give/send some data (by APIs, files etc.)
  * Pydantic checks data is correct or not?
  * If yes → it fixes/correct
  * If no →  throws a clear error message

## Type Hints
Tells Python and Pydantic → What type of data should be here?
→ It's syntax:
  * name:str
  * age: int
  * price: float
  * is_active: bool

→ Python interpreter reads data types internally but do not print data types in output.
→ There are two kinds of types:
  * List Types → A list where every item must be a string (list[str])
  * Optional Types →  can be a string or none (optional[str])

## Real world Impact summary of Pydantic + Type Hints
 * Bad User Input → Validation
 * Wrong Data Types →  Auto Conversion
 * Hidden Bugs →  Early Errors
 * Confusion Code → Type Hint Clarity

## Base Models
 * Base Model is a class/foundation of Pydantic
 * Defines Data Structures
 * Add type rules → using standard python type hints and the field() function for adding constraints
 * Automatically validate + convert data
 * field() function →  Used to provide metadata and validation constraints for modal fields beyond their basic type
                       notations
 * constraints → Conditions or rules that a variable must satisfy for a solution or a program to be considered valid 

```bash
from pydantic import BaseModel

class User(BaseModel):
  name:str
  age:int

# Auto Conversion and valid input (works fine)
user = User(name="Ashish", age=25)
print(user)

# Output: name="Ashish", age=25

# Fields without default values required (age missing)
user = User(name="Ashish")

#Output: field missing error
```

---

```bash
# Optional Field code
from pydantic import BaseModel

class User(BaseModel):
  name:str
  age:int
  city:str="Delhi"

user = User(name="Ashish", age=25)
print(user)

Output: name="Ashish", age=25, city="Delhi"
```

## Custom Validator
 * Custom Validator lets us define our own rules for fields.
 * Not just type checkings, we are enforcing or create our own business logic

```bash
from pydantic import BaseModel, field_validator

class User(BaseModel):
  name:str
  age:int

  @field_validator("age")
  def check_age(cls, v):
    if v < 18:
      raise ValueError("Must be adult")
    return v
```
 * raise → a python keyword used to throw an error (Exception)
 * ValueError → a built-in python error type which gives value wrong or invalid.
 * v → value of the field being validate (actual input value like age)
 * cls → class itself (User)
 * Pydantic Validators are class methods, not instance method.

## Nested Models
 * A model inside another model
 * Used when data is structured/hierarchical

```bash
from pydantic import BaseModel

class Address(BaseModel):
  city:str

class User(BaseModel):
  name:str
  age:str
  address:Address

user = User(name="Ashish", age=25, address={"city":"Delhi"})
print(user)

# Output: name="Ashish", age=25, address=delhi
```
 * Pydantic automatically converts dictionary address into variable address.

## Validation 
Control what data is acceptable.

## Beyond type checking
 * Pydantic validates types, but you often need more:
   → Email must be a valid format
   → Age must be positive
   → Username must be 3-20 characters
   → Price can't be negative

## String constraints
 * Control string length and format:

```bash
from pydantic import BaseModel, Field

class UserProfile(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    bio: str = Field(max_length=500)
    website: str = Field(pattern=r"^https?://.*")

# Valid
profile = UserProfile(
    username="alice_dev",
    bio="Python developer",
    website="https://example.com"
)

# Invalid - username too short
profile = UserProfile(username="ab", bio="Hi", website="https://x.com")
# ValidationError: username must be at least 3 characters
```

String constraints:
 * `min_length` - Minimum number of characters
 * `max_length` - Maximum number of characters
 * `pattern` - Regular expression pattern to match

## Numeric constraints
 * Control number ranges:

```bash
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str
    price: float = Field(gt=0)           # Greater than 0
    quantity: int = Field(ge=0)          # Greater than or equal to 0
    discount: float = Field(ge=0, le=1)  # Between 0 and 1

product = Product(
    name="Widget",
    price=29.99,
    quantity=100,
    discount=0.15
)
```

Numeric constraints:
 * `gt` - Greater than
 * `ge` - Greater than or equal to
 * `lt` - Less than
 * `le` - Less than or equal to

## Pydantic Settings
 * Type-safe configuration from environment variables

## The problem with environment variables
 * Environment variables are strings. Always:

```bash
import os

api_key = os.getenv("API_KEY")           # str | None
max_connections = os.getenv("MAX_CONNECTIONS")  # str | None - not an int!
debug_mode = os.getenv("DEBUG")          # str | None - not a bool!
```

You have to manually:
 → Check if values exist
 → Convert types
 → Validate values
 → Handle defaults

This leads to bugs. Pydantic Settings solves this.

## Installation
 * Pydantic Settings is a separate package. Add it to your project:

```bash
uv add pydantic-settings
```

* If you're following this course, it's already installed via `uv sync`.

## First settings class
 * Create a settings class that reads from environment variables:

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_key: str
    max_connections: int = 100
    debug: bool = False

# Reads from environment variables automatically
settings = Settings()

print(settings.api_key)           # From API_KEY env var
print(settings.max_connections)   # From MAX_CONNECTIONS or default 100
print(settings.debug)             # From DEBUG or default False
```

 * Set environment variables in your shell:

```bash
export API_KEY="sk-abc123"
export MAX_CONNECTIONS="200"
export DEBUG="true"
```

* Then run your Python code. Pydantic reads and validates them automatically.
