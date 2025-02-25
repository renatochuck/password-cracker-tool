#!/usr/bin/env python3
import hashlib
import itertools
import string
import argparse
import time
import concurrent.futures
import subprocess
import socket
import threading
import torch
import torch.nn as nn

# Optimized Hashing function
def hash_password(password, algorithm='md5'):
    if algorithm in hashlib.algorithms_available:
        return hashlib.new(algorithm, password.encode()).hexdigest()
    return None

# Optimized GPU-accelerated cracking using Hashcat (Fully optimized)
def hashcat_crack(hash_to_crack, wordlist=None, algorithm='md5'):
    hash_modes = {'md5': 0, 'sha1': 100, 'sha256': 1400, 'bcrypt': 3200, 'ntlm': 1000}
    if algorithm not in hash_modes:
        return None
    cmd = ["hashcat", "-m", str(hash_modes[algorithm]), "-a", "0" if wordlist else "3", hash_to_crack]
    if wordlist:
        cmd.extend(["-w", "4", wordlist])  # -w 4 for maximum speed on supported systems
    else:
        cmd.append("?a?a?a?a?a?a?a?a")  # Brute-force pattern
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout if "Cracked" in result.stdout else None

# Ultra-fast multi-threaded brute force attack with optimizations
def brute_force_worker(guess, hash_to_crack, algorithm):
    password = ''.join(guess)
    return password if hash_password(password, algorithm) == hash_to_crack else None

def brute_force(hash_to_crack, algorithm='md5', max_length=8, workers=64):
    chars = string.ascii_letters + string.digits + string.punctuation
    for length in range(1, max_length + 1):
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
            futures = [executor.submit(brute_force_worker, guess, hash_to_crack, algorithm)
                       for guess in itertools.product(chars, repeat=length)]
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result:
                    return result
    return None

# Distributed cracking server (Super fast with multiple clients)
def handle_client(client_socket, hash_to_crack, algorithm):
    while True:
        chunk = client_socket.recv(1024).decode()
        if not chunk:
            break
        if hash_password(chunk, algorithm) == hash_to_crack:
            client_socket.send(f"Password cracked: {chunk}".encode())
            break
    client_socket.close()

def start_server(hash_to_crack, algorithm, port=9999):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", port))
    server.listen(10)
    print(f"🚀 High-speed Distributed Cracking Server Started on Port {port}")
    while True:
        client, addr = server.accept()
        threading.Thread(target=handle_client, args=(client, hash_to_crack, algorithm)).start()

# Main function with enhanced speed
def main():
    parser = argparse.ArgumentParser(description="🚀 Ultra-Fast AI-Powered Password Cracker")
    parser.add_argument('hash_to_crack', help="The hash to crack")
    parser.add_argument('--algorithm', choices=['md5', 'sha1', 'sha256', 'bcrypt', 'ntlm'], default='md5', help="Hash algorithm")
    parser.add_argument('--mode', choices=['brute', 'dictionary', 'gpu', 'distributed'], required=True, help="Cracking mode")
    parser.add_argument('--wordlist', help="Path to the wordlist file (required for dictionary mode)")
    parser.add_argument('--max_length', type=int, default=8, help="Max password length for brute-force")
    parser.add_argument('--port', type=int, default=9999, help="Port for distributed cracking server")

    args = parser.parse_args()
    start_time = time.time()

    # Choosing the fastest mode based on user input
    if args.mode == 'gpu':
        password = hashcat_crack(args.hash_to_crack, args.wordlist, args.algorithm)
    elif args.mode == 'brute':
        password = brute_force(args.hash_to_crack, args.algorithm, args.max_length)
    elif args.mode == 'dictionary':
        if not args.wordlist:
            print("❌ Wordlist file is required for dictionary mode.")
            return
        password = hashcat_crack(args.hash_to_crack, args.wordlist, args.algorithm)  # Use Hashcat for dictionary mode
    elif args.mode == 'distributed':
        start_server(args.hash_to_crack, args.algorithm, args.port)
        return

    # Display the result
    if password:
        print(f"\n✅ Password cracked: {password}")
    else:
        print("\n❌ Password not found.")

    end_time = time.time()
    print(f"⏳ Time taken: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
