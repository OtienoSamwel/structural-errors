import math


class Generation:
    def __init__(self, k1, k2, k3, lower_lim, upper_lim, limit_step, used_func):
        self.upper_limit = upper_lim
        self.k1 = k1
        self.k2 = k2
        self.k3 = k3
        self.lower_lim = lower_lim
        self.limit_step = limit_step
        self.upper_lim = upper_lim
        self.used_func = used_func

    def __get_gen_value(self, angle):
        angle_in_radians = math.radians(angle)
        cos_x = math.cos(angle_in_radians)
        sin_x = math.sin(angle_in_radians)
        a = (1 - self.k2) * cos_x - self.k1 + self.k3
        b = -2 * sin_x
        c = self.k1 - (1 + self.k2) * cos_x + self.k3

        gen_value = 2 * math.atan((-b + math.sqrt(b * b - 4 * a * c)) / (2 * a))

        return math.degrees(gen_value).__round__(3)

    def __get_input_angles(self):
        value_range = []
        for i in range(self.lower_lim, self.upper_limit + self.limit_step):
            if i % self.limit_step == 0:
                value_range.append(i)
        return value_range

    def __get_required_output(self):
        required_output = []
        for i in self.__get_input_angles():
            required_output.append(self.used_func(i).__round__(3))
        return required_output

    def __get_generated_output(self):
        generated_output = []
        for angle in self.__get_input_angles():
            generated_output.append(self.__get_gen_value(angle).__round__(3))
        return generated_output

    def __get_error(self):
        error = []
        for i in range(0, len(self.__get_required_output())):
            error.append((self.__get_required_output()[i] - self.__get_generated_output()[i]).__round__(3))
        return error

    def print_table(self):
        for i in range(0, len(self.__get_generated_output())):
            print(str(i + 1) + "       || " + str(self.__get_input_angles()[i]) + "     ||  " + str(
                self.__get_required_output()[i]) + "     ||    " + str(
                self.__get_generated_output()[i]) + "       ||  " + str(self.__get_error()[i]))


# you can try running the code to verify it works with the table on path 27 before you make any changes

# in this function change the return to the given function in the question
def used_function(angle):
    return (245 + (0.35 * angle)).__round__(3)


# in this object init pass in k1, k2, k3, lower_lim, upper_lim, limit_step, used_func
# note the used function is shown above just pass it in as is then run the code
generate = Generation(-9.384, 3.879, 0.296, 20, 150, 5, used_function)

generate.print_table()
