from .Stack import *
from classes.Character import Character, CharacterType, Operator
from .utils.helpers import string_to_array


class ExpressionCalc:
    expression = ""
    operators_stack = Stack[Operator]()
    results_stack = Stack[Character]()
    app_operators: list[Character] = []

    def __init__(self, expression: str) -> None:
        self.expression = expression

    def intfix_to_postfix(self) -> str:
        self.app_operators = get_app_operators("postfix")
        expression_vector = string_to_array(self.expression)

        self.calculator_process(expression_vector)

    def intfix_to_prefix(self) -> str:
        self.app_operators = get_app_operators("prefix")
        expression_vector = string_to_array(self.expression[::-1])

        self.calculator_process(expression_vector)
        self.results_stack.reverse()

    def calculator_process(self, expression_vector):
        for character in expression_vector:
            operator = self.get_is_operator(character)
            if operator == None:
                itemPush = Character(character, CharacterType.Operand)
                self.results_stack.push(itemPush)
            else:
                self.push_character_as_operand(operator)

        while not self.operators_stack.isEmpty():
            self.results_stack.push(self.operators_stack.pop())

    def get_is_operator(self, character: str):
        for key, operator in enumerate(self.app_operators):
            if (operator.symbol == character):
                return operator
        return None

    def push_character_as_operand(self, operator: Operator):
        if operator.type == CharacterType.OpenGroup:
            self.operators_stack.push(operator)
        elif operator.type == CharacterType.CloseGroup:
            while not self.operators_stack.isEmpty():
                if self.operators_stack.peek():
                    if self.operators_stack.peek().type == CharacterType.OpenGroup:
                        self.operators_stack.pop()
                        break

                self.results_stack.push(self.operators_stack.pop())

        else:
            self.check_operators_integrity(operator)

    def check_operators_integrity(self, newOperator: Operator):
        front = self.operators_stack.peek()
        if front:  # front might be None
            if self.operators_stack.peek().type == CharacterType.OpenGroup:
                self.operators_stack.push(newOperator)
                return

            if front.priority == newOperator.priority:
                self.results_stack.push(self.operators_stack.pop())
            elif front.priority > newOperator.priority:
                while not self.operators_stack.isEmpty():
                    if self.operators_stack.peek().type == CharacterType.OpenGroup:
                        break
                    self.results_stack.push(self.operators_stack.pop())
            self.operators_stack.push(newOperator)

        else:
            self.operators_stack.push(newOperator)

    def get_result(self) -> str:
        result = ""
        self.results_stack.reverse()
        while not self.results_stack.isEmpty():
            result += self.results_stack.pop().symbol

        return result


def get_app_operators(method: str):
    result: list[Character] = []

    result.append(Operator('+', 10))
    result.append(Operator('-', 10))
    result.append(Operator('/', 20))
    result.append(Operator('*', 20))
    result.append(Operator('^', 30))

    if method == "postfix":
        result.append(Character('(', CharacterType.OpenGroup))
        result.append(Character(')', CharacterType.CloseGroup))
    elif method == "prefix":
        result.append(Character(')', CharacterType.OpenGroup))
        result.append(Character('(', CharacterType.CloseGroup))

    return result
