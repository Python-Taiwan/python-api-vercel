from Lottery_module import Lottery

class Taiwan_Lottery(Lottery):
  def draw(self):
    print("drawed")

if __name__ == '__main__':
  # for testing purpose
  p = Taiwan_Lottery("ming")
  print(p.name)
  p.draw()
