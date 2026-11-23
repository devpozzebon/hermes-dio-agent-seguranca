import sqlite3
import hashlib
import os

ITERACOES = 100_000  
TAMANHO_SALT = 16    


def _gerar_hash(senha: str) -> str:
    """Gera salt aleatório + hash PBKDF2-HMAC-SHA256.

    Formato de armazenamento: 'salt_hex$hash_hex'
    """
    salt = os.urandom(TAMANHO_SALT)
    dk = hashlib.pbkdf2_hmac('sha256', senha.encode('utf-8'), salt, ITERACOES)
    return f"{salt.hex()}${dk.hex()}"


def _verificar_hash(senha: str, valor_armazenado: str) -> bool:
    """Compara a senha com o valor armazenado, em tempo constante.

    Não vaza informação por diferença de tempo de resposta.
    """
    try:
        salt_hex, hash_hex = valor_armazenado.split('$', 1)
    except ValueError:
        return False
    salt = bytes.fromhex(salt_hex)
    dk = hashlib.pbkdf2_hmac('sha256', senha.encode('utf-8'), salt, ITERACOES)
    return hashlib.compare_digest(dk.hex(), hash_hex)


def fazer_login(usuario: str, senha: str) -> str:
    conexao = sqlite3.connect('banco_de_dados.db')
    try:
        cursor = conexao.cursor()
        .
        cursor.execute(
            "SELECT username, password FROM usuarios WHERE username = ?",
            (usuario,),
        )
        resultado = cursor.fetchone()
    finally:
        conexao.close()

    if resultado is None:
        return "Acesso Negado."

    senha_armazenada = resultado[1]
    if not _verificar_hash(senha, senha_armazenada):
        return "Acesso Negado."

    return "Acesso Permitido!"
