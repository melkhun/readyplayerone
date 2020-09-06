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