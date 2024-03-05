{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "36534799",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "copied to clipboard\n",
      "-995-2024\n"
     ]
    }
   ],
   "source": [
    "import pyperclip\n",
    "import re\n",
    "\n",
    "# phone number regular expressions \n",
    "phoneregex = re.compile(r'''(\n",
    "    (\\d{3}|\\(\\d{3}\\))?  # area code\n",
    "    (\\s|-|\\.)?           # separator\n",
    "    (\\d{3})              # first 3 digits\n",
    "    (\\s|-|\\.)            # separator\n",
    "    (\\d{4})              # last 4 digits\n",
    "    (\\s*(ext|x|ext.)\\s*(\\d{2,5}))?  # extensions\n",
    "    )''', re.VERBOSE)\n",
    "\n",
    "# email pattern regular verification\n",
    "emailregex = re.compile(r'''(\n",
    "    [a-zA-Z0-9._%+-]+     # username \n",
    "    @                     # @ symbol\n",
    "    [a-zA-Z0-9.-]+        # domain name\n",
    "    (\\.[a-zA-Z]{2,4})     # dot-something\n",
    "    )''', re.VERBOSE)\n",
    "\n",
    "# FIND MATCHES IN CLIPBOARD TEXT \n",
    "text = str(pyperclip.paste())\n",
    "matches = []\n",
    "\n",
    "for group in phoneregex.findall(text):\n",
    "    # Initialize variables for phone number parts\n",
    "    area_code = group[1] if group[1] else ''\n",
    "    first_three = group[3]\n",
    "    last_four = group[5]\n",
    "    extension = group[8] if group[8] else ''\n",
    "\n",
    "    # Construct phone number string\n",
    "    phonenum = f\"{area_code}-{first_three}-{last_four}\"\n",
    "    if extension:\n",
    "        phonenum += f\" x{extension}\"\n",
    "\n",
    "    matches.append(phonenum)\n",
    "\n",
    "for group in emailregex.findall(text):\n",
    "    matches.append(group[0])\n",
    "\n",
    "# copy results to the clipboard \n",
    "if len(matches) > 0:\n",
    "    pyperclip.copy('\\n'.join(matches))\n",
    "    print('copied to clipboard')\n",
    "    print('\\n'.join(matches))\n",
    "else:\n",
    "    print(\"No phone numbers or email addresses are identified\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "96e952be",
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
