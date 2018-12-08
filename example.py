# REF README.md
import emojislib as emojis

emoji = emojis.by_name('eyes')
print("name:",emoji.name)
print("char:",emoji.char)
print("category:",emoji.category)
print("keywords:",emoji.keywords)


emoji = emojis.by_cate('animals_and_nature')
print("animals_and_nature",emoji)

emoji = emojis.by_key('winter')
print("winter:",emoji)



