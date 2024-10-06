def areSentencesSimilar(sentence1, sentence2):
    arr1 = list(sentence1.split())
    arr2 = list(sentence2.split())
    while arr1 and arr2 and arr1[0] == arr2[0]:
        arr1.pop(0)
        arr2.pop(0)
    while arr1 and arr2 and arr1[-1] == arr2[-1]:
        arr1.pop()
        arr2.pop()
    if not arr1 or not arr2:
        return True
    return False
