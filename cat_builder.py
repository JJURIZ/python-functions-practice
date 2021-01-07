"""
function catBuilder(name, color, toys) {
  const cat = {
    name: name,
    color: color,
    toys: toys
  };

  return cat;
}
"""
def cat_builder(name, color, toys): 
    cat = {
        "cat_name": name,
        "cat_color": color,
        "cat_toys": toys
    }
    return cat

print(cat_builder("Fluffykins", "Grey", "Laser Pointer"))
