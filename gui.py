import gradio as gr
from app import *

with gr.Blocks(title="Product Management System") as ap:

    gr.Markdown("# 🛒 Product Management System with Groq Gen AI")

    output = gr.Textbox(label="Output", lines=18)

    # -----------------------
    # Top Buttons
    # -----------------------

    with gr.Row():
        load = gr.Button("Load Dummy Data")
        view = gr.Button("View Products")

    load.click(load_dummy_data, outputs=output)
    view.click(display_products, outputs=output)

    # -----------------------
    # Add Product
    # -----------------------

    gr.Markdown("## ➕ Add Product")

    with gr.Row():
        pid = gr.Textbox(label="Product ID")
        name = gr.Textbox(label="Product Name")
        price = gr.Textbox(label="Price")

    add = gr.Button("Add Product")

    add.click(
        add_product,
        inputs=[pid, name, price],
        outputs=output
    )

    # -----------------------
    # Search Product
    # -----------------------

    gr.Markdown("## 🔍 Search Product")

    with gr.Row():
        spid = gr.Textbox(label="Product ID")
        search = gr.Button("Search")

    search.click(
        search_product,
        inputs=[spid],
        outputs=output
    )

    # -----------------------
    # Update Product
    # -----------------------

    gr.Markdown("## ✏ Update Product")

    with gr.Row():
        upid = gr.Textbox(label="Product ID")
        uname = gr.Textbox(label="New Name")
        uprice = gr.Textbox(label="New Price")

    update = gr.Button("Update")

    update.click(
        update_product,
        inputs=[upid, uname, uprice],
        outputs=output
    )

    # -----------------------
    # Delete Product
    # -----------------------

    gr.Markdown("## ❌ Delete Product")

    with gr.Row():
        dpid = gr.Textbox(label="Product ID")
        delete = gr.Button("Delete")

    delete.click(
        delete_product,
        inputs=[dpid],
        outputs=output
    )

    # -----------------------
    # AI Assistant
    # -----------------------

    gr.Markdown("## 🤖 AI Product Assistant")

    query = gr.Textbox(label="Ask AI")
    ai = gr.Button("Ask AI")

    ai.click(
        ai_product_details,
        inputs=[query],
        outputs=output
    )

ap.launch() 