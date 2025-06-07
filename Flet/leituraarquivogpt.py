import flet as ft
import requests
import os
import time

# Configuração segura da API Groq
GROQ_API_KEY = os.getenv("GROQ_API_KEY") or "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"  # Configure a chave no ambiente
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def resposta_chatbot(mensagem, contexto=None, model="llama3-70b-8192", temperature=0.7):
    if not GROQ_API_KEY:
        return "Erro: API Key não configurada."

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    messages = [{"role": "system", "content": "Você é um assistente útil."}]
    
    if contexto:
        messages.append({"role": "user", "content": f"Texto: {contexto}\nPergunta: {mensagem}"})
    else:
        messages.append({"role": "user", "content": mensagem})
    
    payload = {"messages": messages, "model": model, "temperature": temperature, "max_tokens": 4096}

    try:
        response = requests.post(GROQ_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"Erro na conexão: {str(e)}"

def main(page: ft.Page):
    page.title = "ChatBot Groq"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20

    chat_box = ft.ListView(expand=True, spacing=10, auto_scroll=True)
    text_input = ft.TextField(label="Digite sua mensagem", multiline=True, expand=True)
    upload_button = ft.ElevatedButton("📁 Upload Arquivo", on_click=lambda _: pick_files_dialog.pick_files(allow_multiple=False))
    send_button = ft.ElevatedButton("📤 Enviar", icon=ft.icons.SEND)
    clear_button = ft.ElevatedButton("🧹 Limpar", on_click=lambda e: limpar_chat())

    conteudo_arquivo = ""
    
    def pick_files_result(e: ft.FilePickerResultEvent):
        nonlocal conteudo_arquivo
        if e.files:
            conteudo_arquivo = "Arquivo carregado: " + e.files[0].name
            chat_box.controls.append(ft.Text(conteudo_arquivo, color=ft.colors.BLUE_800))
            page.update()
    
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    page.overlay.append(pick_files_dialog)

    def enviar_mensagem(e):
        if not text_input.value.strip():
            return
        
        user_message = text_input.value.strip()
        text_input.value = ""
        
        chat_box.controls.append(ft.Text(f"Você: {user_message}", color=ft.colors.BLUE_800))
        page.update()

        start_time = time.time()
        bot_response = resposta_chatbot(user_message, conteudo_arquivo)
        elapsed_time = time.time() - start_time

        chat_box.controls.append(ft.Text(f"🤖 Bot: {bot_response}\n⏱️ {elapsed_time:.2f}s", color=ft.colors.GREEN_800))
        page.update()
    
    send_button.on_click = enviar_mensagem
    
    def limpar_chat():
        chat_box.controls.clear()
        page.update()
    
    page.add(
        ft.Column([
            ft.Text("ChatBot Groq", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_800),
            chat_box,
            ft.Row([upload_button, clear_button]),
            ft.Row([text_input, send_button])
        ], expand=True)
    )

if __name__ == "__main__":
    ft.app(target=main)
