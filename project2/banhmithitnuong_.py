{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "8f8d07e5-a190-4b4b-ba58-f57717ac4535",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter 'A' for Addition.\n",
      "Enter 'S' for Subtraction.\n",
      "Enter 'M' for Multiplication.\n",
      "Enter 'D' for Division.\n",
      "Enter 'MOD' for Modulo.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter Choice (A, S, M, D, MOD): a\n",
      "Enter first number: 1\n",
      "Enter second number: 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Result:  1.0  +  2.0  =  3.0\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Do you want to continue to the next calculation?(YES/NO): no\n"
     ]
    }
   ],
   "source": [
    "# Instrutions\n",
    "print(\"Enter 'A' for Addition.\")\n",
    "print(\"Enter 'S' for Subtraction.\")\n",
    "print(\"Enter 'M' for Multiplication.\")\n",
    "print(\"Enter 'D' for Division.\")\n",
    "print(\"Enter 'MOD' for Modulo.\")\n",
    "\n",
    "# Addition Calculator\n",
    "def addition_func(first_number, second_number):\n",
    "    return first_number + second_number\n",
    "# Subtraction Calculator\n",
    "def subtraction_func(first_number, second_number):\n",
    "    return first_number - second_number\n",
    "# Multiplication Calculator\n",
    "def multiplication_func(first_number, second_number):\n",
    "    return first_number * second_number\n",
    "# Devision Calculator\n",
    "def division_func(first_number, second_number):\n",
    "    return first_number / second_number\n",
    "# Modulo Calculator\n",
    "def modulo_func(first_number, second_number):\n",
    "    return first_number % second_number\n",
    "\n",
    "while True:\n",
    "    # Input calculation\n",
    "    choice_calculate = input(\"Enter Choice (A, S, M, D, MOD):\").upper()\n",
    "    \n",
    "    if(choice_calculate in (\"A\", \"S\", \"M\", \"D\", \"MOD\")):\n",
    "        try:\n",
    "            # Input first number\n",
    "            first_number = float(input(\"Enter first number:\"))\n",
    "            # Input second number\n",
    "            second_number = float(input(\"Enter second number:\"))\n",
    "            \n",
    "            if(choice_calculate == \"A\"):\n",
    "                print(\"Result: \", first_number, \" + \", second_number, \" = \", addition_func(first_number, second_number))\n",
    "            elif(choice_calculate == \"S\"):\n",
    "                print(\"Result: \", first_number, \" - \", second_number, \" = \", subtraction_func(first_number, second_number))\n",
    "            elif(choice_calculate == \"M\"):\n",
    "                print(\"Result: \", first_number, \" * \", second_number, \" = \", multiplication_func(first_number, second_number))\n",
    "            elif(choice_calculate == \"D\"):\n",
    "                print(\"Result: \", first_number, \" / \", second_number, \" = \", division_func(first_number, second_number))\n",
    "            elif(choice_calculate == \"MOD\"):\n",
    "                print(\"Result: \", first_number, \" % \", second_number, \" = \", modulo_func(first_number, second_number))\n",
    "        \n",
    "        except ValueError:\n",
    "            print(\"Invalid input. Please enter a number.\")\n",
    "        # Next calculation\n",
    "        next_calculation = input(\"Do you want to continue to the next calculation?(YES/NO):\").upper()\n",
    "        if(next_calculation != \"YES\"):\n",
    "            break\n",
    "    else:\n",
    "        print(\"Invalid input. Please enter the correct calculation choice by following the instructions.\") "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0c699d92-22fd-45cf-b9b0-1e446eebd628",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
