from django.shortcuts import render

def calculator(request):
    result = None
    try:
        if request.GET.get("n1") and request.GET.get("n2") and request.GET.get("b1"):
            num1 = float(request.GET.get("n1"))
            num2 = float(request.GET.get("n2"))
            cmd = request.GET.get("b1")
            
            match cmd:
                case "Add":
                    result = num1 + num2
                case "Sub":
                    result = num1 - num2
                case "Mul":
                    result = num1 * num2
                case "Div":
                    result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
    except Exception as e:
        result = f"Error: {e}"

    return render(request, "calculator.html", {"result": result})
