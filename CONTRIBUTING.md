# 🤝 Contributing to BanglaSTT

Thank you for your interest in contributing to BanglaSTT! This guide will help you get started with contributing to our Bangla speech-to-text transcription tool.

## 🌟 Why Contribute?

By contributing to BanglaSTT, you're helping make speech recognition technology more accessible to the 230+ million Bangla speakers worldwide. Every contribution, no matter how small, makes a difference!

## 🚀 Quick Start Guide

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/banglastt.git
cd banglastt
```

### 2. Set Up Development Environment

```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pytest black flake8
```

### 3. Make Your Changes

- Create a new branch for your feature/fix
- Make your changes
- Test thoroughly
- Submit a pull request

## 📝 Types of Contributions

### 🐛 Bug Reports

Found a bug? Help us fix it!

**How to report:**
1. Check if the bug already exists in [Issues](https://github.com/your-repo/issues)
2. Create a new issue with the bug report template
3. Include:
   - Steps to reproduce
   - Expected vs actual behavior
   - System information (OS, Python version)
   - Error messages (if any)
   - Sample files (if relevant)

### 💡 Feature Requests

Have a great idea? Share it with us!

**Popular feature areas:**
- Real-time microphone input
- Batch file processing
- Subtitle file export (SRT)
- Web interface
- Mobile app
- API service
- Better error handling
- Performance improvements

### 🔧 Code Contributions

**Areas where help is needed:**

#### 🎯 Core Improvements
- **Error handling**: Better error messages and recovery
- **Performance**: Optimize transcription speed
- **Memory usage**: Reduce RAM usage for large files
- **Model management**: Automatic model downloading
- **Audio preprocessing**: Noise reduction, normalization

#### 🌍 Platform Support
- **macOS optimization**: Better FFmpeg integration
- **Linux packaging**: .deb, .rpm packages
- **Windows installer**: Setup wizard
- **Docker support**: Containerized deployment

#### 🎨 User Experience
- **GUI application**: Desktop interface
- **Progress bars**: Show transcription progress
- **Better CLI**: More intuitive commands
- **Configuration files**: Save user preferences

#### 📊 Testing & Quality
- **Unit tests**: Test individual functions
- **Integration tests**: Test end-to-end workflows
- **Performance benchmarks**: Speed and accuracy tests
- **Audio samples**: More Bangla test files

### 📝 Documentation

Help make our documentation better!

**Documentation areas:**
- **Tutorials**: Step-by-step guides
- **API documentation**: Function references
- **Video tutorials**: Screen recordings
- **Bangla documentation**: Localized guides
- **Examples**: More usage examples
- **Troubleshooting**: Common issues and solutions

### 🎙️ Audio Samples

Help us test with more Bangla audio!

**We need:**
- Different accents and dialects
- Various audio qualities
- Different speaking speeds
- Background noise samples
- Long-form content (lectures, interviews)
- Short-form content (voice messages, commands)

**Privacy**: Only share audio you have permission to use!

## 🛠️ Development Guidelines

### Code Style

We follow Python best practices:

```python
# Use descriptive function names
def validate_audio_file(file_path: str) -> bool:
    """Validate if the provided file path exists and has a supported audio format."""
    # Implementation here
    pass

# Add type hints
def transcribe_audio(audio_path: str, model_size: str = "base") -> Optional[str]:
    """Transcribe audio file to Bangla text using OpenAI Whisper."""
    pass

# Use meaningful variable names
is_valid = validate_audio_file("audio.mp3")

# Add comprehensive docstrings
def setup_ffmpeg_windows() -> Optional[str]:
    """
    Set up FFmpeg for Windows systems by finding and configuring the executable path.
    
    Returns:
        str: Path to FFmpeg executable if successful, None otherwise
        
    Raises:
        ImportError: If imageio-ffmpeg is not installed
    """
```

### Testing

**Before submitting:**

1. **Run existing tests**:
   ```bash
   pytest tests/
   ```

2. **Test your changes manually**:
   ```bash
   # Test basic functionality
   python transcribe.py test_audio.mp3
   
   # Test with different models
   python transcribe.py test_audio.mp3 --model small
   
   # Test error handling
   python transcribe.py nonexistent.mp3
   ```

3. **Test on different platforms** if possible

### Commit Messages

Use clear, descriptive commit messages:

```bash
# Good examples
feat: add real-time microphone transcription
fix: resolve FFmpeg path issue on Windows 11
docs: update installation guide for Python 3.11
test: add unit tests for audio validation
perf: optimize model loading speed by 40%

# Bad examples
fix stuff
update code
changes
```

### Pull Request Process

1. **Create a descriptive title**
2. **Write a clear description** of changes
3. **Reference related issues** (#123)
4. **Include screenshots** for UI changes
5. **Test thoroughly** before submitting
6. **Be responsive** to feedback

## 🎯 Project Structure

```
banglastt/
├── transcribe.py          # Main transcription script
├── requirements.txt       # Dependencies
├── README.md             # User documentation
├── CONTRIBUTING.md       # This file
├── tests/                # Test files
├── docs/                 # Documentation
├── examples/             # Example audio files
└── utils/                # Utility scripts
```

## 🔍 Code Review Process

**What we look for:**
- ✅ Code follows Python best practices
- ✅ Functions have proper docstrings
- ✅ Error handling is comprehensive
- ✅ Tests are included
- ✅ Documentation is updated
- ✅ No breaking changes (unless necessary)

**Review timeline:** We aim to review PRs within 3-7 days.

## 🎉 Recognition

Contributors will be:
- 📝 Listed in our README.md
- 🏷️ Tagged in release notes
- 🎖️ Given contributor badges
- 📢 Mentioned in our social media

## 📞 Getting Help

**Stuck? Need help?**

1. **Check existing issues** and documentation
2. **Join our discussions** on GitHub
3. **Ask questions** in issue comments
4. **Reach out** to maintainers

**We're here to help!** Don't hesitate to ask questions. Every expert was once a beginner! 😊

## 🌟 Beginner-Friendly Issues

New to open source? Start here!

**Good first issues:**
- 🐛 Fix typos in documentation
- 📝 Add more examples to README
- 🎨 Improve error messages
- 📊 Add more Bangla test audio
- 🔧 Fix code formatting
- ✅ Add unit tests

**Look for the `good-first-issue` label in our issues!**

## 🚀 Advanced Contributions

**For experienced developers:**
- 🎯 Implement real-time transcription
- 🌍 Add multi-language support
- 📱 Create mobile app
- 🌐 Build web interface
- ⚡ Optimize performance
- 🔒 Add security features

## 📚 Learning Resources

**Want to learn more?**

- **Python**: [Python.org tutorial](https://docs.python.org/3/tutorial/)
- **OpenAI Whisper**: [Official documentation](https://github.com/openai/whisper)
- **Git/GitHub**: [GitHub Guides](https://guides.github.com/)
- **Open Source**: [First Contributions](https://github.com/firstcontributions/first-contributions)
- **Speech Recognition**: [Coursera course](https://www.coursera.org/learn/speech-recognition)

## 🎯 Current Priorities

**High priority:**
1. 🐛 Bug fixes and stability
2. 📊 More comprehensive testing
3. 📝 Better documentation
4. 🎙️ More Bangla audio samples

**Medium priority:**
1. ⚡ Performance improvements
2. 🎨 Better user interface
3. 🔧 Enhanced error handling
4. 🌍 Platform-specific optimizations

**Low priority:**
1. 🌐 Web interface
2. 📱 Mobile app
3. 🎯 Real-time transcription
4. 🚀 Advanced features

---

**Thank you for contributing to BanglaSTT!** 🙏

Every contribution, no matter how small, helps make speech recognition more accessible to the Bangla-speaking community. You're not just contributing to a project - you're helping democratize AI technology for millions of people! 🌟

**Ready to start?** Pick an issue, fork the repo, and make your first contribution today! 🚀

---

*Happy coding!* 💻✨