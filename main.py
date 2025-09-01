def suma(a: int, b: int):
    return a+b

def resta(a: int, b: int):
    return a-b

if __name__ == "__main__":
    print(suma(1,2))
    print(resta(1,2))

def bad_quality_function(arg1, arg2, arg3, arg4, arg5, arg6):
    """
    This function is intentionally poorly written to trigger pylint errors.
    """
    var1 = 1
    var2 = 2
    var3 = 3
    var4 = 4
    var5 = 5
    var6 = 6
    var7 = 7
    var8 = 8
    var9 = 9
    var10 = 10
    var11 = 11
    var12 = 12
    var13 = 13
    var14 = 14
    var15 = 15
    var16 = 16
    var17 = 17
    var18 = 18
    var19 = 19
    var20 = 20
    unused_variable = "I am not used"
    
    # This line is way too long and should be flagged by pylint because it exceeds the default line length limit which is typically 100 characters.
    long_line_variable = arg1 + arg2 + arg3 + arg4 + arg5 + arg6 + var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8 + var9 + var10 + var11 + var12 + var13 + var14 + var15 + var16 + var17 + var18 + var19 + var20

    result = (var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8 + var9 + var10 +
              var11 + var12 + var13 + var14 + var15 + var16 + var17 + var18 + var19 + var20)

    print(result)
    print(long_line_variable)
    print(result)
    print(long_line_variable)
    print(result)
    print(long_line_variable)
    print(result)
    print(long_line_variable)
    print(result)
    print(long_line_variable)
    print(result)
    print(long_line_variable)
    print(result)
    print(long_line_variable)
    print(result)
    print(long_line_variable)
    print(result)
    print(long_line_variable)
    print(result)
    print(long_line_variable)
    print(result)
    print(long_line_variable)
    print(result)
    print(long_line_variable)
    print(result)
    print(long_line_variable)
    print(result)
    print(long_line_variable)
    print(result)
    print(long_line_variable)
    print(result)
    print(long_line_variable)
    print(result)
    print(long_line_variable)
    print(result)
    print(long_line_variable)
    print(result)
    print(long_line_variable)
    print(result)
    print(long_line_variable)
    print(result)
    print(long_line_variable)
    print(result)
    print(long_line_variable)
    print(result)
    print(long_line_variable)
    print(result)
    print(long_line_variable)
    return result
