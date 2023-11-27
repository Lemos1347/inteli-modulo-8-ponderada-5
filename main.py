import gradio as gr
from langchain.llms import Ollama
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough


class ChatBot:
    def __init__(self) -> None:
        self.ui = gr.Blocks()
        self.set_up_page()
        self.model = Ollama(
            base_url="http://localhost:11434", model="ppe-assistent")
        
        self._vectoryze_data()
        self._generate_template()
        self._generate_send_question()

    def set_up_page(self):
        with self.ui:
            self.chatbot = gr.Chatbot()
            self.msg = gr.Textbox()
            self.clear = gr.ClearButton([self.msg, self.chatbot])
            self.msg.submit(self.respond, [self.msg, self.chatbot], [
                            self.msg, self.chatbot])

    def respond(self, message, chat_history):
        bot_message = ""
        for s in self.send_question.stream(message):
            bot_message += s
        
        chat_history.append((message, bot_message))
        return "", chat_history

    def launch(self):
        self.ui.launch()
    
    def _vectoryze_data(self):
        loader = TextLoader("./data.txt")
        documents = loader.load()

        text_splitter = CharacterTextSplitter(chunk_size=1097, chunk_overlap=0)
        docs = text_splitter.split_documents(documents)

        embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

        vectorstore = Chroma.from_documents(docs, embedding_function)
        self.vectoryze_data = vectorstore.as_retriever()
    
    def _generate_template(self):
        template = """Answer the question based only on the following context:
                {context}

                Question: {question}
                """
        
        self.prompt = ChatPromptTemplate.from_template(template)

    def _generate_send_question(self):
        self.send_question = (
            {"context": self.vectoryze_data, "question": RunnablePassthrough()} | self.prompt | self.model
        )

if __name__ == "__main__":
    chat = ChatBot()
    chat.launch()
