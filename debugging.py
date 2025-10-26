import logging 

class Debug:
    def calculate(self, a, b):
        try:
            #sum1 = a + b
            sum1 = self.add(a, b)
            logging.info(f"calculate funciton is called with {a} & {b}")
        except:
            logging.warning(f"Error in calculate funciton and is called with {a} & {b}")

    def add(self, a, b):
        logging.debug("add is called ...")
        return a + b


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    obj = Debug()
    obj.calculate(10, 20)