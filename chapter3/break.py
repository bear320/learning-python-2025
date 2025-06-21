for i in "123456789":
    if i == "5":
        print("Breaking the loop at 5")
        break
    print(f"Current number: {i}")
print("Loop has ended.")

# nested loop
for i in "123":
    for j in "abc":
        if j == "b":
            print("Breaking the inner loop at 'b'")
            break
        print(f"Current pair: {i}{j}")
    print(f"Finished processing outer loop with {i}")
