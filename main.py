
### 2. **`main.py`**

```python
from bda import MuzanKibutsuji

def main():
    muzan = MuzanKibutsuji()

    # Example usage
    muzan.set("power", "Biokinesis")
    muzan.set("age", "Over 1000 years")

    try:
        muzan.set("power", "Shape-shifting")
    except ValueError as e:
        print(e)  # Output: Change detected in 'power'. Permanence violated.

    print(muzan.get("age"))  # Output: Over 1000 years

if __name__ == "__main__":
    main()
