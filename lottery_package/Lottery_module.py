class Lottery:
  def __init__(self, name):
    self.name = name
  def draw(self):
    print("WARNING> draw() should be implemented in its child class, not here")

if __name__ == '__main__':
  # for testing purpose
  p1 = Lottery("Taiwan Lottery")
  print(p1.name)
  p1.draw()
