#!/usr/bin/env python
import os
from peft import AutoPeftModelForCausalLM

MODEL_CHECKPOINT = 'timosiebenand/gpt2-instruction'
MODEL_NAME = 'gpt2-instruction'

if __name__ == '__main__':
    # get script directory
    script_dir, _ = os.path.split(os.path.abspath(__file__))
    # load model from HuggingFace
    model = AutoPeftModelForCausalLM.from_pretrained(MODEL_CHECKPOINT)
    # save model locally
    model.save_pretrained(os.path.join(script_dir, MODEL_NAME))
