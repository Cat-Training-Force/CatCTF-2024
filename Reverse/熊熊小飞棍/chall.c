#include <stdint.h>
#include <stdio.h>
#include <string.h>

#define ROUNDS 20

#define QUARTERROUND(a, b, c, d) (                    \
    a += b, d ^= a, d = (d << 16) | (d >> (32 - 16)), \
    c += d, b ^= c, b = (b << 12) | (b >> (32 - 12)), \
    a += b, d ^= a, d = (d << 8) | (d >> (32 - 8)),   \
    c += d, b ^= c, b = (b << 7) | (b >> (32 - 7)))

typedef struct
{
    uint32_t state[16];
} Ctx;

void initia(Ctx *ctx, const uint8_t *key, const uint8_t *nonce, uint32_t counter)
{
    const char *sigma = "expand 32-byte k";
    int i;
    ctx->state[0] = ((uint32_t *)sigma)[0];
    ctx->state[1] = ((uint32_t *)sigma)[1];
    ctx->state[2] = ((uint32_t *)sigma)[2];
    ctx->state[3] = ((uint32_t *)sigma)[3];
    for (i = 0; i < 8; i++)
    {
        ctx->state[4 + i] = ((uint32_t *)key)[i];
    }
    ctx->state[12] = counter;
    ctx->state[13] = ((uint32_t *)nonce)[0];
    ctx->state[14] = ((uint32_t *)nonce)[1];
    ctx->state[15] = ((uint32_t *)nonce)[2];
}

void block(Ctx *ctx, uint8_t *output)
{
    uint32_t x[16];
    int i;
    memcpy(x, ctx->state, sizeof(x));
    for (i = 0; i < ROUNDS; i += 2)
    {
        QUARTERROUND(x[0], x[4], x[8], x[12]);
        QUARTERROUND(x[1], x[5], x[9], x[13]);
        QUARTERROUND(x[2], x[6], x[10], x[14]);
        QUARTERROUND(x[3], x[7], x[11], x[15]);
        QUARTERROUND(x[0], x[5], x[10], x[15]);
        QUARTERROUND(x[1], x[6], x[11], x[12]);
        QUARTERROUND(x[2], x[7], x[8], x[13]);
        QUARTERROUND(x[3], x[4], x[9], x[14]);
    }
    for (i = 0; i < 16; i++)
    {
        x[i] += ctx->state[i];
        ((uint32_t *)output)[i] = x[i];
    }
}
void encrypt(Ctx *ctx, const uint8_t *plaintext, uint8_t *ciphertext, size_t length)
{
    uint8_t cblock[64];
    uint32_t counter = ctx->state[12];
    size_t i = 0;
    size_t j, block_size;

    while (length > 0)
    {
        block(ctx, cblock);
        block_size = length > 64 ? 64 : length;
        for (j = 0; j < block_size; j++)
        {
            ciphertext[i + j] = plaintext[i + j] ^ cblock[j];
        }
        length -= block_size;
        i += block_size;
        ctx->state[12] = ++counter;
    }
}

int main()
{
    uint8_t key[32] = {
        0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07,
        0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f,
        0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17,
        0x18, 0x19, 0x1a, 0x1b, 0x1c, 0x1d, 0x1e, 0x1f};
    uint8_t nonce[12] = {
        0x00, 0x00, 0x00, 0x09,
        0x00, 0x00, 0x00, 0x4a,
        0x00, 0x00, 0x00, 0x00};
    size_t i;
    uint8_t c1[] = {0x73, 0x90, 0x93, 0x87, 0xa5, 0x5d, 0x22, 0x6d, 0x68, 0x39, 0x82, 0x72, 0x93, 0x56, 0x2e, 0xad, 0x94, 0x8e, 0xb4, 0xf6, 0x5f, 0x9f, 0x11, 0x4c, 0x51, 0x7d, 0xe4, 0xa9, 0xa6, 0xb0, 0x11};
    uint8_t c0[32] = {0};
    uint8_t inputbuf[32] = {0};
    Ctx ctx;
    printf("Please input your flag: ");
    scanf("%31s", inputbuf);
    initia(&ctx, key, nonce, 1);
    encrypt(&ctx, inputbuf, c0, 31);
    for (i = 0; i < 31; i++)
    {
        if (c0[i] != c1[i])
        {
            printf("Wrong flag.\n");
            return 0;
        };
    }
    printf("Correct!\n");
    return 0;
}
