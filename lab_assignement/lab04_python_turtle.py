import turtle, random, time

class RunawayGame:
    def __init__(self, canvas, runner, runner2, catcher, catch_radius = 50, init_dist = 400):
        self.canvas = canvas
        self.runner = runner
        self.runner2 = runner2
        self.catcher = catcher
        self.catch_radius2 = catch_radius ** 2
        self.ai_timer_msec = 0

        self.canvas.bgcolor('skyblue')

        # Initialize 'runner', 'runner2' and 'chaser'
        self.runner.shape('turtle')
        self.runner.color('blue')
        self.runner.penup()         # turtle.penup(), pu(), up() : no drawing when moving
        self.runner.setx(-init_dist / 2)
        self.runner.turtlesize(1.5)     # turtle size up
        self.runner.setheading(90)      # to look up(North)

        self.runner2.shape('turtle')
        self.runner2.color('green')
        self.runner2.penup()        # turtle.penup(), pu(), up() : no drawing when moving
        self.runner2.setx(-init_dist / 2)
        self.runner2.sety(-30)
        self.runner2.turtlesize(1.5)  # turtle size up
        self.runner2.setheading(270)  # to look down(South)

        self.catcher.shape('turtle')
        self.catcher.color('red')
        self.catcher.penup()         # turtle.penup(), pu(), up() : no drawing when moving
        self.catcher.setx(+init_dist / 2)
        self.catcher.setheading(180)
        self.catcher.turtlesize(1.5)   # turtle size up
        self.catcher.setheading(90)    # to look up(North)

        # Instantiate an another turtle for drawing
        # hidden turtle
        self.drawer = turtle.RawTurtle(canvas)
        self.drawer.hideturtle()
        self.drawer.penup()

        # Instantiate an another turtle for drawing
        # hidden turtle for score
        self.scoreTurtle = turtle.RawTurtle(canvas)
        self.scoreTurtle.hideturtle()
        self.scoreTurtle.penup()
        self.scoreValue = 0

    def is_catch(self):
        p = self.runner.pos()
        p2 = self.runner2.pos()
        q = self.catcher.pos()
        dx, dy = p[0] - q[0], p[1] - q[1]
        dx2, dy2 = p2[0] - q[0], p2[1] - q[1]
        if dx**2 + dy**2 < self.catch_radius2:
            self.runner.setposition(-200, 0)
            self.runner.setheading(90)
            self.runner2.setposition(-200, -30)
            self.runner2.setheading(270)
            self.catcher.setposition(200, 0)
            self.catcher.setheading(90)
            self.scoreValue += 1
            # return True

        if dx2**2 + dy2**2 < self.catch_radius2:
            self.runner.setposition(-200, 0)
            self.runner.setheading(90)
            self.runner2.setposition(-200, -30)
            self.runner2.setheading(270)
            self.catcher.setposition(200, 0)
            self.catcher.setheading(90)
            self.scoreValue += 3
            # return True
        # return False


    def start(self, ai_timer_msec=100):
        self.ai_timer_msec = ai_timer_msec
        self.start_time = time.time()
        self.canvas.ontimer(self.step, self.ai_timer_msec)

    def step(self):
        self.runner.run_ai(self.catcher)
        self.runner2.run_ai(self.catcher)
        self.catcher.run_ai(self.runner)

        if self.runner.xcor() < -440:
            self.runner.setheading(0)
        if self.runner.xcor() > 440:
            self.runner.setheading(180)
        if self.runner.ycor() < -390:
            self.runner.setheading(90)
        if self.runner.ycor() > 390:
            self.runner.setheading(270)

        if self.runner2.xcor() < -440:
            self.runner2.setheading(0)
        if self.runner2.xcor() > 440:
            self.runner2.setheading(180)
        if self.runner2.ycor() < -390:
            self.runner2.setheading(90)
        if self.runner2.ycor() > 390:
            self.runner2.setheading(270)

        global end_number
        if self.scoreValue >= end_number:           # Game can be end.
            self.scoreTurtle.undo()
            self.scoreTurtle.penup()
            self.scoreTurtle.setpos(-150, 0)
            self.scoreTurtle.color('red', 'white')
            self.scoreTurtle.write(f'Game Over', font=("arial", 35, 'bold'))
            self.canvas.exitonclick()

        # TODO: You can do something here.
        is_caught = self.is_catch()
        self.drawer.undo()
        self.drawer.penup()

        elapse = time.time() - self.start_time

        self.drawer.setpos(-300, 300)
        self.drawer.write(f'Elapsed time : {elapse:.0f} seconds', font=("맑은고딕",15,'bold'))

        self.scoreTurtle.undo()
        self.scoreTurtle.penup()
        self.scoreTurtle.setpos(200, 300)
        self.scoreTurtle.write(f'Your Total Score : {self.scoreValue}', font=("arial", 15, 'bold'))

        self.canvas.ontimer(self.step, self.ai_timer_msec)

class RandomMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

    def run_ai(self, opponent):
        mode = random.random()
        if mode < 0.6:
            self.forward(self.step_move)
        elif mode < 0.9:
            self.left(self.step_turn)
        else:
            self.right(self.step_turn)

class ManualMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

        # Register event handlers
        canvas.onkeypress(lambda: self.forward(self.step_move), 'Up')
        canvas.onkeypress(lambda: self.backward(self.step_move), 'Down')
        canvas.onkeypress(lambda: self.left(self.step_turn), 'Left')
        canvas.onkeypress(lambda: self.right(self.step_turn), 'Right')
        canvas.listen()

    def run_ai(self, opponent):
        pass

if __name__ == '__main__':
    canvas_ = turtle.Screen()
    canvas_.setup(900, 800)
    canvas_.title('Turtle Runaway')

    end_number = turtle.numinput('Input window', 'Enter the game ending score')

    runner_ = RandomMover(canvas_)
    runner2_ = RandomMover(canvas_)
    catcher_ = ManualMover(canvas_)

    game = RunawayGame(canvas_, runner_, runner2_, catcher_)
    game.start()
    canvas_.mainloop()