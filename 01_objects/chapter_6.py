label_text = 'Chai Special'
encoded_label = label_text.encode('utf-8')
print(f'Original label: {label_text}')
decoded_label = encoded_label.decode('utf-16')
print(f'Encoded label: {encoded_label}')
print(f'Decoded label: {decoded_label}')
