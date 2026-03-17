(ALL-IN-ONE-CONVERTER)

A Python-based multi-purpose converter that allows users to convert length, temperature, mass, time, currency, and numerical bases — all through a single interactive menu-driven interface.

📌 Features ✅ Length Unit Converter Meters ↔ Kilometers 🌡️ Temperature Scale Converter Celsius ↔ Fahrenheit ⚖️ Mass Unit Converter Kilograms ↔ Grams ⏱️ Duration Converter Hours ↔ Minutes 💱 Foreign Exchange Converter INR ↔ USD (Uses illustrative, non-live conversion rates) 🔢 Numerical Base Converter Decimal → Binary, Octal, Hexadecimal Binary → Decimal

🛠️ How It Works

The program runs in an infinite loop and displays a main menu with 7 options. The user chooses a category, and the corresponding converter function is executed.

After the conversion, the user is returned back to the main menu until they choose Exit Application. 📂 Project Structure

All-in-One Converter Project │ ├── main.py # Contains all converter functions and main loop └── README.md # Project documentation

▶️ How to Run the Program

1.Install Python (version 3.x recommended)
2.Save your code in a file named main.py
3.Open terminal or command prompt
4.Run: python main.py
5.Choose any option from the menu and start converting! 🧑‍💻 Code Overview Your project contains the following key functions: Function Name Purpose

length_unit_converter() Converts meters ↔ kilometers temp_scale_converter() Converts Celsius ↔ Fahrenheit mass_unit_converter() Converts kilograms ↔ grams duration_converter() Converts hours ↔ minutes foreign_exchange_converter() Converts INR ↔ USD (static rate) numerical_base_converter() Converts between decimal, binary, octal, hex

The main program uses a while True loop to repeatedly show the hub menu.

💡 Sample Menu Interface

===== ALL-IN-ONE-CONVERTER =====

Length Unit Converter
Temperature Scale Converter
Mass Unit Converter
Duration Converter
Foreign Exchange Converter
Numerical Base Converter
Exit Application
📌 Notes

Currency conversion uses fixed sample rates and does NOT fetch live exchange rates.

Program handles invalid menu options using basic validation.

Works in any Python environment (IDLE, VS Code, Terminal, etc.)

🚀 Future Enhancements (Optional)

You may improve the project further by adding:

Live API-based currency conversion

GUI interface using Tkinter / PyQt

Additional units (volume, speed, area, data storage)

Error handling for invalid numeric input

🏁 Conclusion

This All-in-One Converter is a beginner-friendly, well-organized Python project showcasing menus, functions, loops, and basic arithmetic logic — perfect for college submission or learning purposes.
