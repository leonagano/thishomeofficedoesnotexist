import replicate
import webbrowser



# home office design, forest style, metal, 1 desk, 1 chair, bright, 2 windows
# home office design, Lego style, Lego logo, Lego colour palette, 1 desk, 1 chair, bright, 2 windows


output = replicate.run(
    "stability-ai/sdxl:a00d0b7dcbb9c3fbb34ba87d2d5b46c56969c84a628bf778a7fdaec30b1b99c5",
    input={"prompt": " home office design, ancient style, 1 desk, 1 chair, windows", 
        "scheduler": "K_EULER",
        "negative_prompt": "ugly, soft, blurry, out of focus, low quality, garish, distorted, disfigured",
        "guidance_scale": 12,
        "num_inference_steps": 30
    }
)

webbrowser.open(output[0])