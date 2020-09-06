import axios from 'axios'

const base_url = 'http://localhost:8000/app'

export async function getTopGains() {
  const options = {
    method: 'get',
    url: base_url + '/gettopgains'
  }
  let response = await axios(options)
  return response.data
}

export async function getNews() {
  const options = {
    method: 'get',
    url: base_url + '/getnews'
  }
  let response = await axios(options)
  return response.data
}

export async function getCompanySymbol(param) {
  const options = {
    method: 'get',
    url: base_url + `/getcompanysymbol?keyword=${param}`
  }
  let response = await axios(options)
  return response.data
}

export async function getCompanyData(param) {
  const options = {
    method: 'get',
    url: base_url + `/getcompanydata?symbol=${param}`
  }
  let response = await axios(options)
  return response.data
}

export async function getFutures() {
  const options = {
    method: 'get',
    url: base_url + '/getFutures'
  }
  let response = await axios(options)
  return response.data
}

export async function getBonds() {
  const options = {
    method: 'get',
    url: base_url + '/getBonds'
  }
  let response = await axios(options)
  return response.data
}

export async function getOptions() {
  const options = {
    method: 'get',
    url: base_url + '/getOptions'
  }
  let response = await axios(options)
  return response.data
}

export async function getTopETFs() {
  const options = {
    method: 'get',
    url: base_url + '/getTopETFs'
  }
  let response = await axios(options)
  return response.data
}

export async function deletePortfolioAsset(data) {
  const options = {
    method: 'get',
    params: data,
    url: base_url + '/deleteportfolioasset'
  }
  let response = await axios(options)
  return response.data
}

export async function addToPortfolio(data) {
  const options = {
    method: 'get',
    params: data,
    url: base_url + '/addSelectedPortfolio'
  }
  let response = await axios(options)
  return response.data
}

export async function getPortfolio(data) {
  const options = {
    method: 'get',
    params: data,
    url: base_url + '/getUserPortfolio'
  }
  let response = await axios(options)
  return response.data
}

