# emojislib

Emojis for Python 😄 🐍 😋

## Installation


To install the **emojislib** run:

```shell
pip install emojislib
```

## Usage


``emojis.Emojis`` is a dict which contains all emojis available in **emojislib**.There are two main types of methods in emojislib ,`by_` and `search_by_`.

### `by_`...


**by_name**

get one emoji by name

```python
import emojislib as emojis

emoji = emojis.by_name('eyes')

print("name:",emoji.name)
print("char:",emoji.char)
print("category:",emoji.category)
print("keywords:",emoji.keywords)
```

output:

```text
name: eyes
char: 👀
category: people
keywords: ('look', 'watch', 'stalk', 'peek', 'see')
```

**by_cate**

get a list of emoji(s) by category.

```python
emoji = emojis.by_cate('animals_and_nature')
print(emoji)
```
output:

```text
animals_and_nature [ 🐒, 🐵, 🐭, 🐁, 🍄, 🌑, ⚡]
```

**by_key**

get a list of emoji(s) by keywords.

```python
emoji = emojis.by_key('winter')
print("winter:",emoji)
```

```text
winter: [❄️, ⛄, ☃, 🎿, ⛷, 🏂, 🏔]
```

### `search_by_`...

Thers are 3 `search_by_...` methods:

+ `search_by_name`
+ `search_by_key`
+ `search_by_cate`

Just replace **get emoji(s) by a exact str** with **get emoji(s) by a part of a exact str** compared with `by_...`.


