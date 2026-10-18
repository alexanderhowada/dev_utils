#!/usr/bin/env bash


# this code was generated with AI, be careful
# Force standard UTF-8 locale
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

# Detect screen dimensions
if [ "$XDG_SESSION_TYPE" = "wayland" ]; then
    RES=$(kscreen-doctor -o | grep -oE '[0-9]+x[0-9]+' | head -n 1)
    SCREEN_WIDTH=$(echo "$RES" | cut -d 'x' -f 1 | tr -dc '0-9')
    SCREEN_HEIGHT=$(echo "$RES" | cut -d 'x' -f 2 | tr -dc '0-9')
else
    READ_GEO=$(xdpyinfo | awk '/dimensions:/ {print $2}')
    SCREEN_WIDTH=$(echo "$READ_GEO" | cut -d 'x' -f 1 | tr -dc '0-9')
    SCREEN_HEIGHT=$(echo "$READ_GEO" | cut -d 'x' -f 2 | tr -dc '0-9')
fi

SCREEN_WIDTH=${SCREEN_WIDTH:-1920}
SCREEN_HEIGHT=${SCREEN_HEIGHT:-1080}

# Calculate 10% to 90% bounds (X=10%, Y=10%, Width=80%, Height=80%)
X=$(( SCREEN_WIDTH * 10 / 100 ))
Y=$(( SCREEN_HEIGHT * 10 / 100 ))
WIDTH=$(( SCREEN_WIDTH * 80 / 100 ))
HEIGHT=$(( SCREEN_HEIGHT * 80 / 100 ))

# Retry block with state reset & slight delay between actions
for i in {1..3}; do
    WINDOW=$(kdotool getactivewindow 2>/dev/null)
    if [ -n "$WINDOW" ]; then
        # Ensure window is not maximized before resizing
        kdotool windowunmaximize "$WINDOW" 2>/dev/null
        
        # Resize and move with a slight pause for KWin to process
        kdotool windowsize "$WINDOW" "$WIDTH" "$HEIGHT" 2>/dev/null
        sleep 0.02
        kdotool windowmove "$WINDOW" "$X" "$Y" 2>/dev/null
        
        exit 0
    fi
    sleep 0.05
done

exit 1
