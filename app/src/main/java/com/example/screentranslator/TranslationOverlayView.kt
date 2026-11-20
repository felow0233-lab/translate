package com.example.screentranslator

import android.content.Context
import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import android.graphics.Rect
import android.text.Layout
import android.text.StaticLayout
import android.text.TextPaint
import android.view.View

data class TranslatedBlock(val rect: Rect, val translatedText: String)

class TranslationOverlayView(context: Context) : View(context) {

    private var blocks: List<TranslatedBlock> = emptyList()

    private val bgPaint = Paint().apply {
        color = Color.parseColor("#E6141414")
        style = Paint.Style.FILL
    }

    private val textPaint = TextPaint().apply {
        color = Color.WHITE
        isAntiAlias = true
        textSize = 32f
    }

    fun updateTranslations(newBlocks: List<TranslatedBlock>) {
        blocks = newBlocks
        invalidate()
    }

    fun clear() {
        blocks = emptyList()
        invalidate()
    }

    override fun onDraw(canvas: Canvas) {
        super.onDraw(canvas)
        for (block in blocks) {
            val width = (block.rect.width() + 24).coerceAtLeast(120)
            val height = (block.rect.height() + 16).coerceAtLeast(48)
            val left = (block.rect.left - 12).coerceAtLeast(0)
            val top = (block.rect.top - 8).coerceAtLeast(0)

            canvas.drawRect(
                left.toFloat(),
                top.toFloat(),
                (left + width).toFloat(),
                (top + height).toFloat(),
                bgPaint
            )

            textPaint.textSize = (block.rect.height() * 0.45f).coerceIn(24f, 44f)

            val staticLayout = StaticLayout.Builder
                .obtain(block.translatedText, 0, block.translatedText.length, textPaint, (width - 16).coerceAtLeast(60))
                .setAlignment(Layout.Alignment.ALIGN_NORMAL)
                .setLineSpacing(0f, 1.05f)
                .setIncludePad(false)
                .build()

            canvas.save()
            canvas.translate((left + 8).toFloat(), (top + 6).toFloat())
            staticLayout.draw(canvas)
            canvas.restore()
        }
    }
}
