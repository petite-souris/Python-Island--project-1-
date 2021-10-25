# cote UTF-8

# History.
print("Au nord de la plage, tu trouves un petit temple taillé dans la paroi rocheuse.")
print("\nAu-dessus de l'arche d'entrée, il y est écrit un message dans une langue que tu n'arrives pas à discerner : ")
print("\nELHQY HQXHD XGILG XFRGH FVDU !")
print("\nMais tu regardes un détail particulier : cette langue utilise notre alphabet habituel !")
print("\nSur les colonnes de l'arche sont gravées en relief toutes les lettres de l'alphabet.")

# Start of the quest.
print("\nEs-tu curieux de savoir ce qu'il va arriver si tu appuies sur l'une d'elles ?")

# Reply ?
again = input()

# If yes :
if again.upper() != 'N' and again.upper() != 'NON':
    print("\nNous voilà parti pour la quête du code César pour obtenir la clé d'argent !")
        
# If no :
elif again.upper() != 'O' and again.upper() != 'OUI' :
    print("\nNe t'en fais pas, nous comprenons que tu n'est pas prêt encore.")
    print("\nTu pourras revenir quand tu veux pour tenter ta chance.")
    print("\nBon courage à toi petit aventurier !")
        
# Encode the sentence : 'Bienvenue au défi du code César !' with n gap.
alphabet = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
clé = int(input('Choisis un chiffre pour voir la phrase inscrite évoluée : '))

def caesarize_letter(letter, shift):
    if 'A' <= letter.upper() <= 'Z':
        start = ord('a') if letter.islower() else ord('A')
        return chr((ord(letter) - start + shift) % 26 + start)
    else:
        return letter

def caesarize(text, shift):
    return ''.join([caesarize_letter(letter, shift) for letter in text])

def uncaesarize(text, shift):
    return ''.join([caesarize_letter(letter, -1 * shift) for letter in text])

print(caesarize("\nBienvenue au défi du code César !", clé))





