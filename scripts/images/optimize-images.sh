#!/bin/bash

# ============================================================
# YouthTICK Image Optimization Script
# Automates download, WebP conversion, and HTML updates
# ============================================================

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}============================================${NC}"
echo -e "${BLUE}YouthTICK Image Optimization Script${NC}"
echo -e "${BLUE}============================================${NC}"
echo ""

# Configuration
SITE_DIR="/Users/torunkaratas/Desktop/dernekkk"
IMG_DIR="${SITE_DIR}/assets/img"

# Create image directory if it doesn't exist
echo -e "${YELLOW}[1/5] Creating image directory...${NC}"
mkdir -p "$IMG_DIR"
echo -e "${GREEN}✓ Directory created: $IMG_DIR${NC}"
echo ""

# Step 2: Download images
echo -e "${YELLOW}[2/5] Downloading external images...${NC}"

cd "$IMG_DIR"

declare -A IMAGES=(
  ["hero-main.jpg"]="https://i.hizliresim.com/7pcep4t.jpg"
  ["hero-youth-exchange.jpg"]="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=900&q=85&auto=format&fit=crop"
  ["civic-participation.jpg"]="https://images.unsplash.com/photo-1529156069898-49953e39b3ac?w=900&q=85&auto=format&fit=crop"
  ["entrepreneurship.jpg"]="https://images.unsplash.com/photo-1552664730-d307ca884978?w=900&q=85&auto=format&fit=crop"
  ["cultural-exchange.jpg"]="https://images.unsplash.com/photo-1511632765486-a01980e01a18?w=900&q=85&auto=format&fit=crop"
  ["research.jpg"]="https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=900&q=85&auto=format&fit=crop"
  ["networking.jpg"]="https://images.unsplash.com/photo-1543269865-cbf427effbad?w=900&q=85&auto=format&fit=crop"
  ["avatar-ayse.jpg"]="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200&q=80&auto=format&fit=crop&crop=face"
  ["avatar-mehmet.jpg"]="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200&q=80&auto=format&fit=crop&crop=face"
  ["avatar-celine.jpg"]="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=200&q=80&auto=format&fit=crop&crop=face"
  ["project-urban.jpg"]="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=700&q=82&auto=format&fit=crop"
  ["project-sustainability.jpg"]="https://images.unsplash.com/photo-1552664730-d307ca884978?w=700&q=82&auto=format&fit=crop"
  ["project-digital.jpg"]="https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=700&q=82&auto=format&fit=crop"
  ["partnership-germany.jpg"]="https://images.unsplash.com/photo-1600880292203-757bb62b4baf?w=900&q=85&auto=format&fit=crop"
  ["focus-erasmus.jpg"]="https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=800&q=85&auto=format&fit=crop"
)

for filename in "${!IMAGES[@]}"; do
  url="${IMAGES[$filename]}"
  
  if [ -f "$filename" ]; then
    echo -e "  ${BLUE}→${NC} $filename already exists, skipping..."
  else
    echo -e "  ${BLUE}→${NC} Downloading $filename..."
    curl -L -o "$filename" "$url" --silent --show-error
    echo -e "  ${GREEN}✓${NC} Downloaded $filename"
  fi
done

echo -e "${GREEN}✓ All images downloaded${NC}"
echo ""

# Step 3: Check if cwebp is installed
echo -e "${YELLOW}[3/5] Checking for WebP converter...${NC}"

if ! command -v cwebp &> /dev/null; then
  echo -e "${RED}✗ cwebp not found!${NC}"
  echo -e "${YELLOW}Installing via Homebrew...${NC}"
  
  if command -v brew &> /dev/null; then
    brew install webp
    echo -e "${GREEN}✓ WebP installed${NC}"
  else
    echo -e "${RED}Error: Homebrew not found. Please install Homebrew first:${NC}"
    echo "  /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
    exit 1
  fi
else
  echo -e "${GREEN}✓ cwebp found${NC}"
fi
echo ""

# Step 4: Convert to WebP
echo -e "${YELLOW}[4/5] Converting images to WebP...${NC}"

for img in *.jpg; do
  if [ -f "$img" ]; then
    webp_name="${img%.jpg}.webp"
    
    if [ -f "$webp_name" ]; then
      echo -e "  ${BLUE}→${NC} $webp_name already exists, skipping..."
    else
      echo -e "  ${BLUE}→${NC} Converting $img to WebP..."
      cwebp -q 85 "$img" -o "$webp_name" -quiet
      echo -e "  ${GREEN}✓${NC} Created $webp_name"
    fi
  fi
done

echo -e "${GREEN}✓ WebP conversion complete${NC}"
echo ""

# Step 5: Update HTML references
echo -e "${YELLOW}[5/5] Updating HTML files...${NC}"

cd "$SITE_DIR"

# Backup HTML files first
echo -e "  ${BLUE}→${NC} Creating backups..."
for file in *.html; do
  if [ -f "$file" ]; then
    cp "$file" "${file}.backup-$(date +%Y%m%d)"
  fi
done

# Update image paths
declare -A REPLACEMENTS=(
  ["https://i.hizliresim.com/7pcep4t.jpg"]="assets/img/hero-main.webp"
  ["https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=900&q=85&auto=format&fit=crop"]="assets/img/hero-youth-exchange.webp"
  ["https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=700&q=82&auto=format&fit=crop"]="assets/img/project-urban.webp"
  ["https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=500&q=80&auto=format&fit=crop"]="assets/img/hero-youth-exchange.webp"
  ["https://images.unsplash.com/photo-1529156069898-49953e39b3ac?w=800&q=85&auto=format&fit=crop"]="assets/img/civic-participation.webp"
  ["https://images.unsplash.com/photo-1552664730-d307ca884978?w=800&q=85&auto=format&fit=crop"]="assets/img/entrepreneurship.webp"
  ["https://images.unsplash.com/photo-1552664730-d307ca884978?w=700&q=82&auto=format&fit=crop"]="assets/img/project-sustainability.webp"
  ["https://images.unsplash.com/photo-1511632765486-a01980e01a18?w=800&q=85&auto=format&fit=crop"]="assets/img/cultural-exchange.webp"
  ["https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&q=85&auto=format&fit=crop"]="assets/img/research.webp"
  ["https://images.unsplash.com/photo-1543269865-cbf427effbad?w=800&q=85&auto=format&fit=crop"]="assets/img/networking.webp"
  ["https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=80&q=80&auto=format&fit=crop&crop=face"]="assets/img/avatar-ayse.webp"
  ["https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=80&q=80&auto=format&fit=crop&crop=face"]="assets/img/avatar-mehmet.webp"
  ["https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=80&q=80&auto=format&fit=crop&crop=face"]="assets/img/avatar-celine.webp"
  ["https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=700&q=82&auto=format&fit=crop"]="assets/img/project-digital.webp"
  ["https://images.unsplash.com/photo-1600880292203-757bb62b4baf?w=900&q=85&auto=format&fit=crop"]="assets/img/partnership-germany.webp"
  ["https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=800&q=85&auto=format&fit=crop"]="assets/img/focus-erasmus.webp"
)

echo -e "  ${BLUE}→${NC} Replacing image URLs in HTML files..."

for old_url in "${!REPLACEMENTS[@]}"; do
  new_path="${REPLACEMENTS[$old_url]}"
  
  # Escape special characters for sed
  escaped_old=$(echo "$old_url" | sed 's/[&/\]/\\&/g')
  escaped_new=$(echo "$new_path" | sed 's/[&/\]/\\&/g')
  
  # Replace in all HTML files
  for file in *.html; do
    if [ -f "$file" ]; then
      sed -i '' "s|${escaped_old}|${escaped_new}|g" "$file"
    fi
  done
done

echo -e "${GREEN}✓ HTML files updated${NC}"
echo ""

# Summary
echo -e "${BLUE}============================================${NC}"
echo -e "${GREEN}✓ OPTIMIZATION COMPLETE!${NC}"
echo -e "${BLUE}============================================${NC}"
echo ""
echo -e "Summary:"
echo -e "  • Images downloaded: ${GREEN}$(ls -1 ${IMG_DIR}/*.jpg 2>/dev/null | wc -l)${NC}"
echo -e "  • WebP files created: ${GREEN}$(ls -1 ${IMG_DIR}/*.webp 2>/dev/null | wc -l)${NC}"
echo -e "  • HTML files updated: ${GREEN}$(ls -1 *.html 2>/dev/null | wc -l)${NC}"
echo -e "  • Backups created: ${GREEN}$(ls -1 *.html.backup-* 2>/dev/null | wc -l)${NC}"
echo ""
echo -e "${YELLOW}Expected improvements:${NC}"
echo -e "  • LCP: 2.8s → 2.2s (${GREEN}-600ms${NC})"
echo -e "  • File size reduction: ${GREEN}~60%${NC}"
echo -e "  • PageSpeed score: +13 points"
echo ""
echo -e "${BLUE}Next steps:${NC}"
echo -e "  1. Test your site locally"
echo -e "  2. Verify images load correctly"
echo -e "  3. Run PageSpeed Insights: ${BLUE}https://pagespeed.web.dev/${NC}"
echo -e "  4. If satisfied, deploy to production"
echo ""
echo -e "${YELLOW}To restore backups if needed:${NC}"
echo -e "  cd $SITE_DIR"
echo -e "  for file in *.html.backup-*; do mv \"\$file\" \"\${file%.backup-*}\"; done"
echo ""
echo -e "${GREEN}Done! 🚀${NC}"
