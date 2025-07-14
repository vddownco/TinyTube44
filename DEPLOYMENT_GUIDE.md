# 🚀 TinyTube PythonAnywhere Deployment Guide

## Step 1: Create PythonAnywhere Account
1. Go to [pythonanywhere.com](https://www.pythonanywhere.com)
2. Sign up for a free Beginner account
3. Verify your email and log in

## Step 2: Upload Your Files
1. Go to the **Files** tab in your PythonAnywhere dashboard
2. Navigate to `/home/yourusername/mysite/` (replace `yourusername` with your actual username)
3. Upload all your project files:
   - `app.py`
   - `wsgi.py`
   - `requirements.txt`
   - `templates/` folder (with all HTML files)
   - `static/` folder (if you have CSS/JS files)

## Step 3: Install Dependencies
1. Go to the **Consoles** tab
2. Start a **Bash console**
3. Run these commands:
   ```bash
   cd ~/mysite
   pip3.10 install --user -r requirements.txt
   ```

## Step 4: Configure Web App
1. Go to the **Web** tab
2. Click **"Add a new web app"**
3. Choose **"Manual configuration"**
4. Select **Python 3.10**
5. Click **Next**

## Step 5: Configure WSGI File
1. In the **Web** tab, find the **"Code"** section
2. Click on the **WSGI configuration file** link
3. Replace the entire content with:
   ```python
   import sys
   import os
   
   # Add your project directory to the Python path
   path = '/home/yourusername/mysite'  # Replace 'yourusername' with your actual username
   if path not in sys.path:
       sys.path.insert(0, path)
   
   from app import app as application
   
   if __name__ == "__main__":
       application.run()
   ```
4. **Important:** Replace `yourusername` with your actual PythonAnywhere username
5. Save the file

## Step 6: Set Static Files (Optional)
1. In the **Web** tab, scroll to **"Static files"** section
2. Add:
   - URL: `/static/`
   - Directory: `/home/yourusername/mysite/static/`

## Step 7: Reload and Test
1. Click the green **"Reload"** button in the Web tab
2. Click on your domain link (e.g., `yourusername.pythonanywhere.com`)
3. Your TinyTube app should now be live! 🎉

## Troubleshooting

### If you get import errors:
```bash
pip3.10 install --user Flask yt-dlp
```

### If downloads don't work:
- Check that the `tmp` folder has write permissions
- Free accounts have limited CPU seconds - downloads may timeout for large files

### If the app doesn't load:
1. Check the **Error log** in the Web tab
2. Make sure all file paths in `wsgi.py` use your correct username
3. Ensure all files are uploaded to the correct directory

## Important Notes for Free Accounts:
- ⏰ **CPU seconds limit**: Free accounts have daily CPU limits
- 📁 **Storage limit**: 512MB total storage
- 🌐 **Custom domain**: Not available on free accounts
- ⚡ **Performance**: May be slower than paid accounts

## Your App URL:
After deployment, your TinyTube will be available at:
`https://yourusername.pythonanywhere.com`

---
**Made with ❤️ by Sanket | Deployed on PythonAnywhere**