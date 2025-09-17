#!/usr/bin/env python3
"""
BanglaSTT - Bangla Speech-to-Text Transcription Tool

A professional Bangla speech recognition tool powered by OpenAI Whisper.
This module provides functionality to transcribe audio files in Bangla language
with proper error handling and cross-platform compatibility.

Author: Ratul
License: MIT
"""

import argparse
import os
import sys
from pathlib import Path
from typing import Optional, Dict, Any

# Core dependencies
try:
    import whisper
except ImportError:
    print("❌ Error: OpenAI Whisper is not installed. Please install it using:")
    print("   pip install openai-whisper")
    sys.exit(1)

# Windows-specific FFmpeg setup
def setup_ffmpeg_windows() -> Optional[str]:
    """
    Set up FFmpeg for Windows systems by finding and configuring the executable path.
    
    Returns:
        str: Path to FFmpeg executable if successful, None otherwise
    """
    try:
        import imageio_ffmpeg
        ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()
        
        # Set environment variables for FFmpeg
        os.environ["IMAGEIO_FFMPEG_EXE"] = ffmpeg_path
        ffmpeg_dir = os.path.dirname(ffmpeg_path)
        os.environ["PATH"] = ffmpeg_dir + os.pathsep + os.environ.get("PATH", "")
        
        print(f"✅ FFmpeg configured: {os.path.basename(ffmpeg_path)}")
        return ffmpeg_path
        
    except ImportError:
        print("⚠️  Warning: imageio-ffmpeg not found, FFmpeg may not work properly")
        return None


def patch_whisper_ffmpeg(ffmpeg_path: str) -> None:
    """
    Monkey patch Whisper's audio loading to use the correct FFmpeg path on Windows.
    
    Args:
        ffmpeg_path: Full path to FFmpeg executable
    """
    import whisper.audio
    import subprocess
    from subprocess import CalledProcessError
    import numpy as np
    
    def patched_load_audio(file: str, sr: int = 16000) -> np.ndarray:
        """
        Load audio file using FFmpeg with proper path resolution.
        
        Args:
            file: Path to audio file
            sr: Sample rate (default: 16000)
            
        Returns:
            np.ndarray: Audio waveform as float32 array
        """
        cmd = [
            ffmpeg_path,  # Use full path instead of just "ffmpeg"
            "-nostdin",
            "-threads", "0",
            "-i", file,
            "-f", "s16le",
            "-ac", "1",
            "-acodec", "pcm_s16le",
            "-ar", str(sr),
            "-"
        ]
        
        try:
            out = subprocess.run(cmd, capture_output=True, check=True).stdout
        except CalledProcessError as e:
            raise RuntimeError(f"Failed to load audio: {e.stderr.decode()}") from e
        
        return np.frombuffer(out, np.int16).flatten().astype(np.float32) / 32768.0
    
    # Apply the patch
    whisper.audio.load_audio = patched_load_audio


def validate_audio_file(file_path: str) -> bool:
    """
    Validate if the provided file path exists and has a supported audio format.
    
    Args:
        file_path: Path to the audio file
        
    Returns:
        bool: True if file is valid, False otherwise
    """
    supported_formats = {'.mp3', '.wav', '.m4a', '.mp4', '.webm', '.mpeg', '.mpga'}
    
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"❌ Error: File '{file_path}' does not exist.")
        return False
    
    # Check file extension
    file_extension = Path(file_path).suffix.lower()
    if file_extension not in supported_formats:
        print(f"❌ Error: Unsupported audio format '{file_extension}'.")
        print(f"📋 Supported formats: {', '.join(sorted(supported_formats))}")
        return False
    
    return True


def transcribe_audio(audio_path: str, model_size: str = "base", save_output: bool = False) -> Optional[str]:
    """
    Transcribe audio file to Bangla text using OpenAI Whisper.
    
    Args:
        audio_path: Path to the audio file
        model_size: Whisper model size (tiny, base, small, medium, large)
        save_output: Whether to save transcription to output.txt
        
    Returns:
        str: Transcribed text if successful, None if error occurs
    """
    try:
        print(f"🔄 Loading Whisper model '{model_size}'...")
        model = whisper.load_model(model_size)
        
        print(f"🎤 Transcribing audio file: {os.path.basename(audio_path)}")
        print("⏱️  This may take a few minutes depending on file size...")
        
        # Transcribe the audio
        result = model.transcribe(audio_path, language="bn")
        
        transcription = result["text"].strip()
        
        # Display the transcription
        print("\n" + "="*60)
        print("📝 BANGLA TRANSCRIPTION:")
        print("="*60)
        print(transcription)
        print("="*60)
        
        # Save to file if requested
        if save_output:
            output_file = "output.txt"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(transcription)
            print(f"\n💾 Transcription saved to: {output_file}")
        
        return transcription
        
    except FileNotFoundError:
        print(f"❌ Error: Audio file '{audio_path}' not found.")
        return None
    except RuntimeError as e:
        print(f"❌ Error: Failed to load Whisper model. {str(e)}")
        return None
    except Exception as e:
        print(f"❌ Error during transcription: {str(e)}")
        return None


def create_argument_parser() -> argparse.ArgumentParser:
    """
    Create and configure the argument parser for command-line arguments.
    
    Returns:
        argparse.ArgumentParser: Configured argument parser
    """
    parser = argparse.ArgumentParser(
        description="BanglaSTT - Bangla Speech-to-Text using OpenAI Whisper",
        epilog="💡 Example: python transcribe.py audio_file.mp3",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        usage="%(prog)s [options] audio_file"
    )
    
    # Required arguments
    parser.add_argument(
        "audio_file",
        help="Path to the audio file (MP3, WAV, M4A, etc.)"
    )
    
    # Optional arguments
    parser.add_argument(
        "-m", "--model",
        choices=["tiny", "base", "small", "medium", "large"],
        default="base",
        help="Whisper model size (default: base)"
    )
    
    parser.add_argument(
        "-o", "--output",
        action="store_true",
        help="Save transcription to output.txt"
    )
    
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output"
    )
    
    return parser


def main() -> None:
    """
    Main function to handle command-line arguments and execute transcription.
    """
    # Parse command-line arguments
    parser = create_argument_parser()
    args = parser.parse_args()
    
    # Set up FFmpeg for Windows
    ffmpeg_path = setup_ffmpeg_windows()
    if ffmpeg_path:
        patch_whisper_ffmpeg(ffmpeg_path)
    
    # Validate audio file
    if not validate_audio_file(args.audio_file):
        sys.exit(1)
    
    # Perform transcription
    transcription = transcribe_audio(
        args.audio_file,
        model_size=args.model,
        save_output=args.output
    )
    
    if transcription is None:
        sys.exit(1)
    
    # Display summary
    print(f"\n✅ Transcription completed successfully!")
    print(f"📁 Audio file: {args.audio_file}")
    print(f"🤖 Model used: {args.model}")
    print(f"📝 Text length: {len(transcription)} characters")
    
    # Additional processing info
    if args.verbose:
        print(f"🔧 FFmpeg path: {ffmpeg_path or 'System default'}")
        print(f"🎯 Language: Bengali (bn)")


if __name__ == "__main__":
    main()