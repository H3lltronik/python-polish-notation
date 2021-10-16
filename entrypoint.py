from classes.ExpressionCalc import ExpressionCalc 

calculator = ExpressionCalc("K+L-M*N*O+(L+V/Y*Z)")

calculator.intfix_to_postfix()
print(f"intfix {calculator.expression} -> postfix: {calculator.get_result()}")
calculator.intfix_to_prefix()
print(f"intfix {calculator.expression} -> prefix: {calculator.get_result()}")