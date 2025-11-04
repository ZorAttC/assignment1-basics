#!/usr/bin/env python3
"""
Script to split TinyStories dataset into smaller proportional test sets.

Usage:
    python split_tinystories.py --input_file data/TinyStoriesV2-GPT4-valid.txt --output_file test_sample.txt --ratio 0.1

This will create a new file with 10% of the stories randomly sampled from the input file.
"""

import argparse
import random
import os

def load_stories(file_path):
    """Load stories from a TinyStories file, split by <|endoftext|>."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by the end-of-text token
    stories = content.split('<|endoftext|>')
    
    # Remove empty strings and strip whitespace
    stories = [story.strip() for story in stories if story.strip()]
    
    return stories

def sample_stories(stories, ratio):
    """Randomly sample a proportion of stories."""
    num_samples = int(len(stories) * ratio)
    if num_samples < 1:
        num_samples = 1  # At least one story
    
    sampled = random.sample(stories, num_samples)
    return sampled

def save_stories(stories, output_file):
    """Save stories to a file, joined by <|endoftext|>."""
    content = '<|endoftext|>'.join(stories)
    if content:
        content += '<|endoftext|>'  # Add final token
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Saved {len(stories)} stories to {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Split TinyStories into smaller test sets.')
    parser.add_argument('--input_file', type=str, required=True, help='Path to input TinyStories file')
    parser.add_argument('--output_file', type=str, required=True, help='Path to output file')
    parser.add_argument('--ratio', type=float, required=True, help='Proportion of stories to sample (0.0 to 1.0)')
    parser.add_argument('--seed', type=int, default=42, help='Random seed for reproducibility')
    
    args = parser.parse_args()
    
    if not (0.0 < args.ratio <= 1.0):
        raise ValueError("Ratio must be between 0.0 and 1.0")
    
    if not os.path.exists(args.input_file):
        raise FileNotFoundError(f"Input file {args.input_file} does not exist")
    
    random.seed(args.seed)
    
    print(f"Loading stories from {args.input_file}...")
    stories = load_stories(args.input_file)
    print(f"Found {len(stories)} stories")
    
    print(f"Sampling {args.ratio*100:.1f}% of stories...")
    sampled_stories = sample_stories(stories, args.ratio)
    
    save_stories(sampled_stories, args.output_file)

if __name__ == '__main__':
    main()