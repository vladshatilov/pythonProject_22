class Unit:
    def __init__(self, x_coord: int, y_coord: int, direction, state, speed: float = 1):
        self.x = x_coord
        self.y = y_coord
        self.speed = speed
        self.direction = direction
        self.state = state

    def _get_speed_info(self):
        if self.state == 'is_fly':
            return self.speed * 1.2
        elif self.state == 'crawl':
            return self.speed * 0.5
        else:
            return self.speed

    def move(self, field, direction):

        self.speed = self._get_speed_info()

        if direction == 'UP':
            field.set_unit(x=self.x, y=self.y + self.speed, unit=self)
        elif direction == 'DOWN':
            field.set_unit(x=self.x, y=self.y - self.speed, unit=self)
        elif direction == 'LEFT':
            field.set_unit(x=self.x - self.speed, y=self.y, unit=self)
        elif direction == 'RIGHT':
            field.set_unit(x=self.x + self.speed, y=self.y, unit=self)

