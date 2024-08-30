**Muzan-Kibutsuji** is a CLI tool inspired by the character Muzan Kibutsuji from *Demon Slayer: Kimetsu no Yaiba*. This tool embodies Muzan's characteristics—cold-hearted, ruthless, and unwavering in its pursuit of perfection—by ensuring permanence and immutability in data handling.

![Muzan](./images/muzan_1.gif)

## Features

- **Immutable Data Handling**: Once a value is set, it cannot be changed, representing Muzan's unyielding nature.
- **Data Integrity**: Uses checksums to detect and prevent changes to existing data.
- **Assimilation**: Integrate data from other instances without altering existing values.
- **Purging**: Removes data but only if it exists, maintaining strict order.

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Muzan-Kibutsuji.git
cd Muzan-Kibutsuji
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the main CLI tool:

```bash
python main.py
```

### Example

Here’s a basic example of how to use the `MuzanKibutsuji` class:

```python
from bda import MuzanKibutsuji

muzan = MuzanKibutsuji()

muzan.set("power", "Biokinesis")
muzan.set("age", "Over 1000 years")

try:
    muzan.set("power", "Shape-shifting")
except ValueError as e:
    print(e)  # Output: Change detected in 'power'. Permanence violated.

print(muzan.get("age"))  # Output: Over 1000 years
```

## Blood Demon Art

Muzan's Blood Demon Art (BDA) is implemented as a module that provides additional features to manipulate and control data in unique ways, mimicking Muzan's fearsome powers.

![Muzan](https://64.media.tumblr.com/ba6be1a0349e981ee63a2d14b0092c13/9ccc4b7bd50e0fa5-c6/s540x810/6fbfa81cc92fd9f584789944a4a734903c5eca8b.gif)

### Key Methods

- **`set(key: str, value: Any)`**: Sets a value if it doesn't exist or hasn't changed.
- **`get(key: str)`**: Retrieves a value if it exists.
- **`assimilate(other: MuzanKibutsuji)`**: Assimilates another instance without altering existing values.
- **`purge(key: str)`**: Removes a key-value pair, but only if it exists.
- **`eternal_view()`**: Provides an unchanging view of all data.

## Contribution

Contributions are welcome! Please feel free to submit issues or pull requests. Any contributions that enhance the tool's capabilities while maintaining the core principles of permanence and immutability are greatly appreciated.

## License

This project is licensed under the MIT License.

![Muzan](https://cdn.shopify.com/s/files/1/0400/9767/7479/files/Demon-Slayer-Muzan-Kibutsuji-threatening-a-demon.png?v=1681162747)
