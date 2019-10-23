<template>
	<view>
		<web-view :src="webUrl"></web-view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				webUrl: ''
			}
		},
		methods: {
			
		},
		onLoad(mData) {
			this.webUrl = mData.webUrl,
			console.log("--->",this.webUrl)
		}
	}
</script>

<style>

</style>
