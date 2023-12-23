import tkinter as tk
import secrets
from tkinter import font
from encryption import encrypt, decrypt  # Import encryption/decryption functions


def start_app():
    """Starts the UI for the sentence encryption program."""

    def encrypt_action():
        """Encrypts the text and displays the result."""
        try:
            text = text_input.get("1.0", "end-1c")  # Get text from input
            shift = (
                secrets.randbelow(26)
                if shift_var.get() == 1
                else int(shift_input.get())
            )
            encrypted_text = encrypt(text, shift)  # Uses the imported encrypt function
            output_text.config(state="normal")  # Enable editing
            output_text.delete("1.0", "end")  # Clear previous output
            output_text.insert(
                "1.0", str(encrypted_text)
            )  # Insert new output as a string
            output_text.config(state="disabled")  # Disable editing
        except:
            pass

    def decrypt_action():
        """Decrypts the text and displays the result."""
        try:
            text = text_input.get("1.0", "end-1c")  # Get text from input
            shift = (
                secrets.randbelow(26)
                if shift_var.get() == 1
                else int(shift_input.get())
            )
            decrypted_text = decrypt(text, shift)  # Uses the imported decrypt function
            output_text.config(state="normal")  # Enable editing
            output_text.delete("1.0", "end")  # Clear previous output
            output_text.insert("1.0", decrypted_text)  # Insert new output
            output_text.config(state="disabled")  # Disable editing
        except:
            pass

    def clear_action():
        text_input.delete("1.0", "end")  # Clear input text
        output_text.config(state="normal")  # Enable editing
        output_text.delete("1.0", "end")  # Clear output text
        output_text.config(state="disabled")  # Disable editing

    root = tk.Tk()
    root.title("Sentence Encryptor")

    # Organize UI elements using frames
    main_frame = tk.Frame(root)
    main_frame.pack(padx=20, pady=20)  # Add padding for spacing

    # Title label
    title_label = tk.Label(
        main_frame, text="Sentence Encryptor", font=("Helvetica", 18, "bold")
    )
    title_label.pack(pady=10)

    # Input section
    input_frame = tk.Frame(main_frame)
    input_frame.pack()

    text_label = tk.Label(input_frame, text="Enter your sentence:")
    text_label.pack()
    text_input = tk.Text(input_frame, height=5, width=40)
    text_input.pack()

    # Shift options section
    shift_frame = tk.Frame(main_frame)
    shift_frame.pack(pady=10)

    shift_var = tk.IntVar(value=1)  # Default to random shift
    random_shift_radio = tk.Radiobutton(
        shift_frame, text="Encrypt with random shift", variable=shift_var, value=1
    )
    custom_shift_radio = tk.Radiobutton(
        shift_frame, text="Encrypt with custom shift:", variable=shift_var, value=2
    )
    shift_label = tk.Label(shift_frame, text="Shift value (0-25):")
    shift_input = tk.Entry(shift_frame, width=5)

    random_shift_radio.pack(side=tk.LEFT)
    custom_shift_radio.pack(side=tk.LEFT)
    shift_label.pack(side=tk.LEFT)
    shift_input.pack(side=tk.LEFT)

    # Output section
    output_frame = tk.Frame(main_frame)
    output_frame.pack(pady=10)

    output_label = tk.Label(output_frame, text="Result:")
    output_label.pack()
    output_text = tk.Text(
        output_frame, height=5, width=40, state="disabled"
    )  # Initially disabled
    output_text.pack()

    # Action buttons
    buttons_frame = tk.Frame(main_frame)
    buttons_frame.pack()

    encrypt_button = tk.Button(buttons_frame, text="Encrypt", command=encrypt_action)
    decrypt_button = tk.Button(buttons_frame, text="Decrypt", command=decrypt_action)
    clear_button = tk.Button(
        buttons_frame, text="Clear", command=clear_action
    )  # Add clear button

    encrypt_button.pack(side=tk.LEFT, padx=5)
    decrypt_button.pack(side=tk.LEFT, padx=5)
    clear_button.pack(side=tk.LEFT)

    root.mainloop()
