#2.2 implement a class called player that represents a circket player.the player class should have a medhod called play()which prints'the player is playiing cricket.derive two classes.override the play()method in each derived class to print'the bastsman is batting' and 'the bastsman is batting'and 'the bowler is bowling',respectively.write a program to create objects of both the batsman and bowler classes and call the play() method for each object.
class player:

  def play(self):
    print("the player is playing cricket.")


class batsman(player):

  def play(self):
    print("the batsman is batting.")


class bowler(player):

  def play(self):
    print("the bowler is bowling.")


batsman_obj = batsman()
batsman_obj.play()

bowler_obj = bowler()
bowler_obj.play()
