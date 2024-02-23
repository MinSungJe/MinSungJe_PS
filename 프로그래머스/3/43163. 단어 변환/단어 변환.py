from collections import deque

def solution(begin, target, words):
    answer = 0
    visited = [False for _ in range(len(words))]
    queue = deque([(begin, 0)])
    
    while queue:
        word, count = queue.popleft()
        
        if word == target:
            answer = count
            break
        
        for letter_idx in range(len(word)):
            for letter in list(map(chr, range(97, 123))):
                word_ = ''
                for idx in range(len(word)):
                    if idx == letter_idx: word_ += letter
                    else: word_ += word[idx]
                
                for words_idx in range(len(words)):
                    if words[words_idx] != word_: continue
                    if visited[words_idx]: continue
                    
                    visited[words_idx] = True

                    queue.append((word_, count+1))
        
    return answer